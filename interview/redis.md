<div align='center'><img src='https://github.com/czp-first/ToBeBetter/blob/master/icons/redis.svg'></div>

# 数据类型

## String(字符串)

key/value键值对，二进制安全(string可以包含任何数据)，string类型的值最大能存储512MB



### 实现方式

内部结构是一个带信息的字节数组。有两种存储方式，在长度特别短时，使用embstr形式存储，而长度超过44字节时，使用raw形式存储



### 使用场景

- 常规key-value缓存应用
- 常规计数：粉丝数、访问量统计
- 将数据以二进制序列化的方式进行存储
- 分布式系统生成子增长id
- 共享session



## Hash(字典)

是一个key/value键值对的集合



### 实现方式

字典结构内部包含了两个HashTable，通常情况下只有一个HashTable是有值的，但是在字典扩容缩容时，需要重新分配新的HashTable，然后进行<font color='red'>渐进式搬迁</font>，这时候两个HashTable存储的分别是旧的HashTable和新的HashTable，搬迁结束后，旧的HashTable被删除，新的HashTable取而代之。

大字典的扩容是比较耗时的，需要重新申请新的数组，然后将旧字典所有链表中的元素重新挂接到新的数组下面，这是一个O(n)级别的操作，作为单线程的redis很难承受这样耗时的过程，所以redis使用<font color='red'>渐进式rehash小步搬迁</font>，虽然慢一点，但是肯定可以搬完。

### 使用场景

- 存储、读取、修改对象属性



## List(列表)

简单的字符串列表，按照插入顺序排序

### 实现方式

<font color='red'>双向链表</font>，底层实现不是一个简单的LinkedList，而是快速链表(quicklist)。当列表元素较少时，会使用一块连续的内存存储，这个结构是ziplist，即压缩列表。它将所有的元素彼此紧挨着一起存储，分配的是一块连续的内存；当数据量比较多的时候才会改成quicklist。

普通的链表需要的附加指针空间太大，会浪费空间，加重内存的碎片化。redis将链表和ziplist结合起来组成quicklist，也就是将多个ziplist使用双向指针串联起来使用，即满足了快速的插入删除性能，又不会出现太大的空间冗余。

越接近两端的元素访问越快，但是通过索引访问时会比较慢

### 使用场景

- 消息队列
- 最新消息排行



## Set(集合)

string类型的无序集合，集合是一堆不重复值的组合

### 实现方式

通过hashtable实现，只不过value永远为null，实际就是通过计算hash的方式来快速排重的，这也是set能提供判断一个成员是否在集合内的原因。当set集合容纳的元素都是整数并且元素个数较少时，reids会使用intset来存储集合元素。intset是紧凑的数组结构，同时支持16位、32位和64位整数

set中的元素没有顺序，添加、删除、查找的复杂度都是O(1)

### 使用场景

- 共同好友
- 统计访问网站的所有ip
- 好友推荐，根据tag求交集，大于某个阈值就可以推荐
- 全局去重



## Sorted Set(有序集合)

和set一样也是string类型元素的集合，且每个元素关联了一个double类型权重参数score。往有序集合中插入数据时会自动根据这个分数排序

### 实现方式

内部使用HashMap和<font color='red'>跳跃表(SkipList)</font>来保证数据的存储和有序，HashMap里放的是成员到score的映射，而跳跃表里存放的是所有的成员，排序依据是HashMap里存的score，使用跳跃表的结构可以获得比较高的查找效率，并且在实现上比较简单

redis的跳表共有64层，能容纳2的64次方个元素

redis之所以用跳表来实现有序集合

- 插入、删除、查找以及迭代输出有序序列这几个操作，<font color='red'>红黑树</font>都可能完成，时间复杂度和跳表是一样的。但是按照区间来查找数据，红黑树的效率就没有跳表高
- 跳表更容易代码实现，比起红黑树来说更好懂、更好写、可读性更好
- 跳表更加灵活，可以通过改变索引构建策略，有效平衡执行效率和内存消耗

### 使用场景

- 排行榜，取TopN操作
- 带权重的消息队列



# redisObject(robj)

## 字符串

redis的字符串叫 sds(simple dynamic string)。它的机构是一个带长度信息的字节数组。



sds源码

```c++
struct sdshdr{ 
  //记录buf数组中已使用字节的数量 
  int len;
  //记录 buf 数组中未使用字节的数量 
  int free; 
  //字符数组，用于保存字符串
  char buf[];
}

```



字符串对象的存储对应三种编码格式

- int：int类型的整数
- embstr：编码的简单动态字符串，小字符串，长度小于44个字节
- raw：简单动态字符串，大字符串，长度大于44个字节



## dict(字典)

字典是redis服务器中出现最为频繁的复合型数据结构，除了hash结构的数据会用到字典外，整个redis数据库的所有key和value也组成了一个全局字典，还有带过期时间的key集合也是一个字典，zset中存储value和score值的映射关系也是通过字典结构实现的。



dict源码

```c++
typedef struct dict { 
  dictType *type; // 该字典对应的特定操作函数 
  void *privdata; // 上述类型函数对应的可选参数 
  dictht ht[2]; /* 两张哈希表，存储键值对数据，ht[0]为原生ht[1]为 rehash 哈希表 */ 
  long rehashidx; /*rehash标识 当等于-1时表示没有在否则表示正在进行rehash操作，存储的值表示 ht[0]的rehash进行到哪个索引值hash表 (数组下标)*/ 
  int iterators; // 当前运行的迭代器数量 
  } dict;

```



hashtale源码

```c++
struct dictEntry { 
  void* key ; 
  void* val ; 
  dictEntry* next;//链接 下一个entry 
  } 
  
struct dictht { 
  dictEntry** table; // 哈希表数组 
  long size ; // 哈希表数组的大小 
  long used ; // 哈希表中已有节点的数量 
  // ... 
  }

```



字典的内部为什么包含两个hashtable

另一个是在扩容的时候用的，通常情况下只有一个hashtable是有值的，但是在字典扩容缩容时，需要分配新的hashtable，然后进行渐进式搬迁，这时候两个hashtable存储的分别是旧的hashtable和新的hashtable。待搬迁结束后，旧的hashtable被删除，新的hashtable取而代之。



### 字典的扩容

假设两个hashtable分别是h[0]、h[1]

条件：达到扩容阈值

流程

1. 申请新内存，新内存地址赋值给h[1]
2. 将rehashidx置为0，表示要进行rehash操作
3. 将增加的数据存到hash[1]
4. 执行查找、更新、删除命令，现在ht[0]中查找，没有找到再去ht[1]中找
5. 将老的hash表h[0]的数据重新计算索引值后全部迁移到新的hash表h[1]中，这个过程称为 rehash



## ziplist(压缩列表)

redis为了节约内存空间使用，zset和hash容器对象在元素个数较少的时候，采用压缩列表(ziplist)进行存储。压缩列表是一块连续的内存空间，元素之间紧接着存储，没有任何冗余空隙。

源码

```c++
struct ziplist<T> { 
    int32 zlbytes ; //整个压缩列表占用字节数 
    int32 zltail_offset; //最后一个元素距离压缩列表起始位直的偏移量，用于快速定位到最后一个节点 
    int16 zllength ; //元素个数 
    T[] entries ; //元素内容列表，依次紧凑存储 
    int8 zlend; //标志压缩列表的结束，值恒为 OxFF 
}
  
struct entry{ 
    int<var> prevlen; // 前一个 entry 的字节长度 
    int<var> encoding; // 元素类型编码 
    int<var> len; // 当前entry的长度 
    optional byte[] content; // 元素内容
    //... 
}

```



## intset(小整数集合)

当set集合容纳的元素都是整数并且元素个数较少时，redis会使用intset来存储集合元素。intset是紧凑的数组结构，同时支持16位、32位和64位整数。不满足上述条件时，set集合结构的底层实现是字典，只不过所有的value都是null，其他特性和字典一样。



## quickList(快速列表)

quicklist是一个双向链表，链表中的每个节点是一个ziplist结构。quicklist中的每个节点ziplist都能够存储多个数据元素

源码

```c++
typedef struct quicklist { 
  quicklistNode *head; // 指向quicklist的头部 
  quicklistNode *tail; // 指向quicklist的尾部 
  unsigned long count; // 列表中所有数据项的个数总和 
  unsigned int len; // quicklist节点的个数，即ziplist的个数 
  int fill : 16; // ziplist大小限定，由list-max-ziplist-size给定(Redis设定) 
  unsigned int compress : 16; // 节点压缩深度设置，由list-compress-depth给定(Redis设定) 
  } quicklist;
  
  typedef struct quicklistNode {
    struct quicklistNode *prev; // 指向上一个quicklistNode节点
    struct quicklistNode *next; // 指向下一个quicklistNode节点
    unsigned char *zl; // 数据指针，如果没有被压缩，就指向ziplist结构，反之指向quicklistLZF结构
    unsigned int sz; // 表示指向ziplist结构的总长度(内存占用长度)
    unsigned int count : 16; // 表示ziplist中的数据项个数
    unsigned int encoding : 2; // 编码方式，1--ziplist，2--quicklistLZF
    unsigned int container : 2; // 预留字段，存放数据的方式，1--NONE，2--ziplist
    unsigned int recompress : 1; // 解压标记
    // ...
}quicklistNode;    

```



## skipList(跳跃列表)





# 过期策略

在redis内部，当设置一个键的过期时间时，redis就会将该键带上过期时间存放到一个过期字典中。当查询一个键时，redis便首先检查该键是否存在过期字典中，如果存在，那就获取其过期时间。然后将过期时间和当前系统时间进行比对，比系统时间大，那就没有过期；反之则判定该键过期。

**redis的过期删除策略是：惰性删除和定期删除两种策略配合使用**

## 定时删除

在设置某个key的过期时间同时，会创建一个定时器，让定时器在该过期时间到来时，立即执行对其删除的操作

### 优点

对内存最友好，能够保证内存的key一旦过期就能立即从内存中删除

### 缺点

对cpu最不友好，在过期键比较多的时候，删除过期键会占用一部分cpu时间，对内存的响应时间和吞吐量造成影响

## 惰性删除

设置该key过期时间后，redis不会去管他，当需要该key时，redis再检查是否过期，如果过期，redis就会删除它，反之返回该key。

由 db.c/expirelfNeeded 函数实现，所有键读写命令执行之前都会调用 expirelfNeeded 函数对其进行检查，如果过期，则删除该键，然后执行键不存在的操作；未过期则不做操作，继续执行原有命令。

### 优点

对cpu友好，reis只会在使用该键时才会进行过期检查，对于很多用不到的key不用浪费时间进行过期检查

### 缺点

对内存不友好，如果一个键已经过期，但是一直没有使用，那么该键就会一直存在内存中，如果redis有很多这种使用不到的过期键，这些键便永远不会被删除，内存永远不会释放。从而造成内存泄露。

## 定期删除

每隔一段时间，redis就对一些key进行检查，删除里面过期的key。

由 redis.c/activeExpireCycle 函数实现，函数以一定的频率运行，每次运行时，都从一定数量的数据库中取出一定数量的随机键进行检查，并删除其中的过期键。注意，并不是一次运行就检查所有的库、所有的键，而是随机检查一定数量的键。

采用一种简单的[贪心策略](https://zh.wikipedia.org/wiki/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)

1. 从过期字典中随机20个key
2. 删除这20个key中已经过期的key
3. 如果过期的key比例超过1/4，就重复步骤1

### 优点

可以通过限制删除操作执行的时常和频率来减少删除操作对cpu的影响，另外也能有效释放过期键占用的内存

### 缺点

- 最重要的是，在获取某个键时，如果某个键的过期时间已经到了，但是还没有执行定期删除，那么就会返回这个键的值，这是业务不能忍受的错误

- 难以确定删除操作执行的时长和频率
- 如果执行的太频繁，定期删除策略会变得和定时删除策略一样，对cpu不友好
- 如果执行的太少，那就会变得和惰性删除一样了，过期键占用的内存不会及时得到释放



## AOF、RDB对过期键的处理

### 生成RDB文件

在执行save或bgsave命令创建一个新的RDB文件时，程序会对数据库中的键进行检查，已过期的键不会保存到新的RDB文件中。

### 载入RDB文件

- 如果服务器已主服务器模式运行，那么在载入RDB文件时，过期的键会被过滤掉，不会被载入到redis中。
- 如果服务器以从服务器模式运行，那么无论键是否过期都会被载入到数据库中。但因为主从服务器在进行数据同步时，从服务器就会被清空，所以一般来说过期键对从服务器也不对造成影响。

### AOF文件写入

当服务器开启AOF运行模式时，如果某个键过期了，但没有被惰性或定期删除，那么AOF不会理会。如果被惰性或定期删除了，AOF会在文件末尾追加一条 DEL 命令，来显示的记录该键已被删除。

### AOF重写

当AOF重写时，过期的键不会被载入到redis中。



# 淘汰策略

对于某些永远使用不到的键，并且多次定期删除也没选定到并删除，这些键会一直驻留在内存中，又或者在redis中存入了大量的键，这些操作可能导致redis内存不够用，这时候就需要redis的内存淘汰策略了。

## 设置redis最大内存

在配置文件redis.conf中，可以通过参数 maxmemory \<bytes\> 来设定最大内存，不设定该参数默认是无限制的

## 设置内存淘汰方式

redis中的[LRU算法](https://github.com/czp-first/ToBeBetter/tree/master/algorithm/lru)是近似LRU算法

[LFU算法](https://github.com/czp-first/ToBeBetter/tree/master/algorithm/lfu)

当现有内存大于 maxmemory 时，便会触发redis主动淘汰内存方式，通过设置 maxmemory-policy，有如下几种淘汰方式

- noeviction：不移除任何key，只是返回一个写错误。**默认选项，一般不会选用**
- volatile-ttl：移除即将过期的key
- volatile-lru：利用LRU(Least Recently Used)算法移除设置过过期时间的key
- allkeys-lru：利用LRU算法移除任何key(包括未设置过期时间的key)
- volatile-random：移除设置过过期时间的随机key
- always-random：无差别的随机移除
- volatile-lfu：利用LFU(Least Frequently Used)算法移除设置过过期时间的key
- allkeys-lfu：利用LFU算法移除任何key(包括未设置过期时间的key)



# 持久化

数据都存储在内存当中，在处理客户端请求时，所有操作都在内存中进行，只要服务器关机，内存中的数据就会消失，不仅服务器关机会造成数据消失，redis服务器守护进程退出，内存中的数据也一样会消失。



为了避免内存中数据丢失，redis提供了对持久化的支持，将数据从内存中保存到硬盘当中。redis提供了RDB(redis database)和AOF(append only file)两种不同的数据持久化方式。

## RDB(redis database)

RDB是一种快照存储持久化方式，具体就是将redis某一时刻的内存数据保存到硬盘的文件当中，而在redis服务器启动时，会重新加载文件的数据到内存当中恢复数据。

三种方式

- save命令
- bgsave命令
- 自动触发



### 触发方式

#### save命令

当客户端向服务器发送save命令请求持久化时，服务器会阻塞save命令之后的其他客户端亲故，直到数据同步完成。如果数据量太大，同步数据会执行很久，而这期间redis服务器无法接收其他请求，所以醉话不要在生产环境使用save命令

#### bgsave命令

异步保存数据到磁盘上

当客户端向服务器发送bgsave命令，redis服务器主进程会forks一个子进程来同步数据，在讲数据保存到rdb文件之后，子进程会退出。与save命令相比，redis服务器在处理bgsave采用子线程进行IO写入，而主进程仍然可以接收其他请求，但forks子进程是同步的，所以forks子进程时一样不能接收其他请求，这意味着，如果forks一个子进程花费的时间太久(一般是很快的)，bgsave命令仍然有阻塞其他客户端请求的情况发生。

#### 自动触发

在redis配置文件中的save指定到达触发RDB持久化的条件，比如【多少秒内至少达到多少写操作】就开始RDB数据同步。

这种通过服务器配置文件触发RDB的方式，与bgsave命令类似，达到触发条件时，会forks一个子进程进行数据同步，不过通过这种方式来触发RDB持久化，如果设置触发的时间太短，则容易频繁写入rdb文件，影响服务器性能，时间设置太长则会造成数据丢失。



### 优点

- 与AOF相比，通过rdb文件恢复数据比较快
- rdb文件非常紧凑，适合于数据备份
- 通过RDB进行数据备份，由于使用子进程生成，所以对redis服务器性能影响较小



### 缺点

- 如果服务器宕机，采用RDB方式会造成某个时间段内的数据丢失
- 使用save命令会造成服务器阻塞，直到数据同步完成后才能接收后续请求
- 使用bgsave命令在forks子进程时，如果数据量太大，forks的过程也会发生阻塞，另外，forks子进程会耗费内存



## AOF(append only file)

AOF持久化方式会记录客户端对服务器的每一次写操作命令，并将这些写操作以redis协议追加保存到一后缀为aof文件末尾，在redis服务器重启时，会加载并运行aof文件的命令，进行恢复数据。默认不开启AOF持久化。aof文件是一个二进制文件

### 三种写入策略

#### always

客户端的每一个写操作都保存到aof文件中，这种策略很安全，但是每一写请求都有IO操作，所以也很慢

#### everysec

appendsync的默认写入策略，每秒写入一次aof文件，因此，最多可能会丢失1s的数据

#### no

redis服务器不负责写入aof，而是交由操作系统来处理什么时候写入aof文件。更快，但也是最不安全的选择，不推荐使用



### AOF文件重写

AOF将客户端的每一个写操作都追加到aof命令末尾，可能会造成aof文件变得非常大。aof文件太大，加载aof文件恢复数据时，就会非常慢，为了解决这个问题，reids支持aof文件重写，通过重写aof，可以生成一个恢复当前数据的最少命令集。

#### 

### 两种重写方式

1. 在redis配置文件中的选项 no-appendfsync-on-rewrite 可以设置是否开启重写，这种方式会在每次fsync时都会重写，影响服务器性能，因此默认值为no，不推荐使用
2. 客户端向服务器发送bgrewriteaof命令，也可以让服务器进行AOF重写。



### 重写aof的好处

- 压缩aof文件，减少磁盘占用量
- 将aof的命令压缩为最小命令集，加快了数据恢复的速度



### AOF文件损坏

```
redis-check-aof -fix file.aof
```



### 优点

AOF只是追加日志文件，因此对服务器性能影响较小，速度比RDB要快，消耗的内存较少

### 缺点

- AOF方式生成的日志文件太大，即使通过AOF重写，文件体积仍然很大
- 恢复数据的速度比RDB慢



当RDB与AOF两种都开启时，redis会优先使用AOF来恢复数据，因为AOF保存的文件比RDB文件更完整。

# 参考资料

[10 分钟彻底理解 Redis 的持久化和主从复制](https://mp.weixin.qq.com/s/ZGamPtfIZaMwUk1DU3iDnQ)

[Redis 几种数据类型及应用场景](https://juejin.cn/post/6844903951502934030)

[Redis五种数据类型及应用场景](https://blog.51cto.com/u_14612575/2740299)

[Redis详解（十一）------ 过期删除策略和内存淘汰策略 ](https://www.cnblogs.com/ysocean/p/12422635.html)

[聊聊 Redis 的过期键删除策略](https://segmentfault.com/a/1190000040130962)