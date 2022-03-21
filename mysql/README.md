<div align='center'><img src='https://github.com/czp-first/ToBeBetter/blob/master/icons/mysql.svg'></div>



# 0 总体架构

<div align='center'><img src='https://img-blog.csdnimg.cn/20210402013609534.png#pic_center'></div>

<div align='right'><span>-- 摘自</span><a href='https://blog.csdn.net/huangzhilin2015/article/details/115396599'>MySQL--buffer pool、redo log、undo log、binlog</a></div>

# 1 索引

索引是一种数据结构，用于帮助我们在**大量**数据中快速定位到目标数据。注意大量，数据量大了索引才显得有意义。

## 1.1 索引类型

<table>
    <tr>
        <td>维度</td>
        <td>索引名称</td>
    </tr>
    <tr>
        <td rowspan="4">数据结构维度</td>
        <td>B+树索引</td>
    </tr>
    <tr>
        <td>哈希索引</td>
    </tr>
  	<tr>
        <td>全文索引</td>
    </tr>
  	<tr>
        <td>R-Tree索引</td>
    </tr>
    <tr>
        <td rowspan="2">物理存储维度</td>
        <td>聚集索引</td>
    </tr>
    <tr>
        <td>非聚集索引</td>
    </tr>
    <tr>
        <td rowspan="5">逻辑维度</td>
        <td>主键索引</td>
    </tr>
    <tr>
        <td>普通索引</td>
    </tr>
    <tr>
        <td>唯一索引</td>
    </tr>
      <tr>
        <td>联合索引</td>
    </tr>
    <tr>
        <td>空间索引</td>
    </tr>
</table>


### 1.1.1 聚簇索引

- 如果表设置了主键，则主键就是聚簇索引
- 如果表没有主键，则会默认第一个`NOT NULL`，且唯一（`UNIQUE`）的列作为聚簇索引
- 以上都没有，则会默认创建一个隐藏的row_id作为聚簇索引

InnoDB的聚簇索引的叶子节点存储的是行记录（其实是页结构，一个页包含多行数据），InnoDB必须至少要有一个聚簇索引。由此可见，使用聚簇索引查询会很快，因为可以直接定位到行记录。

如果查询条件位主键（聚簇索引），则只需扫描一个B+树即可通过聚簇索引定位到要查找的行记录数据。

### 1.1.2 普通索引

普通索引也叫二级索引，除索引外的索引，即非聚簇索引。

InnoDB的普通索引叶子节点存储的是主键（聚簇索引）的值，而MyISAM的普通索引记录的是记录指针。

如果查询条件为普通索引（非聚簇索引），可能需要扫描两次B+树，第一次扫描通过普通索引定位到聚簇索引的值，然后第二次扫描通过聚簇索引的值定位到要查找的行记录数据，查询非索引列数据。

<font color='red'>使用普通索引不一定会回表</font>



## 1.2 回表查询

先通过普通索引的值定位聚簇索引值，再通过聚簇索引的值定位行记录数据，需要扫描两次索引B+树，它的性能较扫一遍索引树更低。



## 1.3 覆盖索引

只需要在一棵索引树上就能获取SQL所需的所有列数据，无需回表，速度更快。

explain分析：Extra列的值为Using index

使用索引覆盖来优化SQL的场景

- 全表count查询优化
- 列查询回表优化
- 分页查询



## 1.4 索引下推

Index Condition Pushdown，简称ICP，是MySQL5.6版本的新特性，它能减少`回表`查询次数，提高查询效率，也可以减少MySQL Server层从引擎层接收数据的次数

索引下推的下推其实就是指将部分Server层负责的事情，交给了引擎层去处理

### 1.4.1 不ICP的查询过程

- 存储引擎读取索引记录
- 根据索引中的主键值，定位并读取完整的行记录
- 存储引擎把记录交给Server层去检测该记录是否满足WHERE条件

### 1.4.2 使用ICP的查询过程

- 存储引擎读取索引记录（不是完整的行记录）
- 判断WHERE条件部分能否用索引中的列来检查，条件不满足，则处理下一行索引记录
- 条件满足，使用索引中的主键去定位并读取完整的行记录（回表）
- 存储引擎把记录交给Server层，Server层检测该记录是否满足WHERE条件的其余部分



### 1.4.3 explain分析

Extra列有Using index condition，但是并不代表一定使用了索引下推，只是代表可以使用



### 1.4.4 使用条件

- 联合索引

- 只能用于`range`、`ref`、`eq_ref`、`ref_or_null` 访问方法

- 只能用于`InnoDB`和`MyISAM`存储引擎及其分区表

- 对`InnoDB`存储引擎来说，索引下推只适用于普通索引。（索引下推的目的是为了减少回表次数。对于`InnoDB`的聚簇索引来说，数据和索引是在一起的，不存在回表这一说）
- 使用子查询的条件不能下推
- 使用存储函数的条件不能下推，因为存储引擎无法调用存储函数



## 1.5 索引结构

### 1.5.1 B-树与B+树的区别

- B-树内部节点是保存数据的；而B+树内部节点是不保存数据的，只起索引作用，它的叶子节点才保存数据
- B+树相邻的叶子节点之间是通过链表指针连起来的，B-树却不是
- 查找过程中，B-树在找到具体的数值以后就结束，而B+树可以出现多次



### 1.5.2 为什么索引结构默认使用B+树

- 二叉树
- 平衡二叉树
- B树(Balance Tree)
- B+树



几点

- 树的高度 => 查询效率、磁盘io
- 节点存储的数据量 => 磁盘io



## 1.6 mysql索引在什么情况下会失效

- 查询条件包括or，可能导致索引失效
- 如果字段类型是字符串，where时一定用引号括起来，否则索引失效。因为会做隐式转换
- like通配符可能导致索引失效
- 联合索引，查询时的条件列不是联合索引中的第一个列，索引失效
- 在索引列上使用mysql的内置函数，索引失效
- 在索引列运算（如：+、-、*、\），索引失效
- 索引字段上使用（!= 、<>、not in）时，可能导致索引失效
- 索引字段上使用is null，is not null，可能导致索引失效
- 左连接查询或者右连接查询，查询关联的字段编码格式不一样，可能导致索引失效。
- mysql估计使用全表扫描要比使用索引快，则不使用索引



## 1.7 索引不适合哪些场景

- 数据量少的不适合加索引
- 更新比较频繁的不适合加索引
- 区分度低的字段不适合加索引



# 2 存储引擎

## 2.1 mysql的存储引擎InnoDB与MyISAM的区别

- InnoDB支持事务，MyISAM不支持事务
- InnoDB支持外键，MyISAM不支持外键
- InnoDB支持MVCC（多版本并发控制），MyISAM不支持
- select count(*) from table时，MyISAM更快，因为它有一个变量保存了整个表的总行数，可以直接读取，InnoDB就需要全表扫描
- InnoDB不支持全文索引，而MyISAM支持全文索引（5.7以后的InnoDB也支持全文索引）
- InnoDB支持表、行级锁，而MyISAM支持表级锁
- InnoDB表必须有主键，而MyISAM可以没有主键
- InnoDB表需要更多的内存和存储，而MyISAM可被压缩，存储空间较小
- InnoDB按主键大小有序插入，MyISAM记录插入顺序时，按记录插入顺序保存
- InnoDB存储引擎提供了具有提交、回滚、崩溃恢复能力的事务安全，与MyISAM比，InnoDB写的效率差一些，并且会占用更多的磁盘空间以保留数据和索引



# 3 事务

有一个有限的数据库操作序列构成，这些操作要么全部执行，要么全部不执行，是一个不可分割的工作单位。

## 3.1 四大特性

- 原子性(Atomicity)：事务作为一个整体被执行，包含在其中的对数据库的操作要么全部都执行，要么都不执行。
- 一致性(Consistency)：指在事务开始之前和事务结束以后，数据不会被破坏，假如A账户给B账户转10块钱，不管成功与否，A和B的总金额是不变的。
- 隔离性(Isolation)：多个事务并发访问时，事务之间是相互隔离的，一个事务不应该被其他事务干扰，多个并发事务之间要相互隔离。
- 持久性(Durabilily)：表示事务完成提交后，该事务对数据库所做的操作更改，将持久地保存在数据库之中。



## 3.2 原子性

<a href='#undo'>undo日志</a>(回滚日志)



## 3.3 持久性

<a href='#redo'>redo log</a>(重做日志)



## 3.4 隔离性

一个事务写操作对另一个事务写操作的影响：锁机制保证隔离性。

一个事务写操作对另一个事务读操作的影响：MVCC保证隔离性。

### 3.4.1 锁机制

隔离性要求同一时刻只能有一个事务对数据进行写操作，InnoDB通过锁机制来保证这一点。

锁机制的基本原理可以概括为：事务在修改数据之前，需要先获得相应的锁；获得锁之后，事务便可以修改数据；该事务操作期间，这部分数据是锁定的，其他事务如果需要修改数据，需要等待当前事务提交或回滚后释放锁。

按照粒度，锁可以分为表锁、行锁以及其他位于二者之间的锁。



### 3.4.2 读操作可能存在的三类问题

- 脏读(dirty read)：事务A、B交替执行，事务A读取到事务B未提交的数据。
- 不可重复读(unrepeatable read)：事务A内，先后两次读取同一条记录，两次读取的结果却不一样。
- 幻读：事务A查询一个范围的结果集，另一个并发事务B往这个范围中插入/删除了数据，并静悄悄地提交了，然后事务A再次查询相同的范围，两次读取得到的结果集不一样了。

脏读和不可重复读的区别在于：前者读到的是其他事务未提交的数据，后者读到的是其他事务已提交的数据。

不可重复读与幻读的区别可以通俗的理解为：前者是数据变了，后者是数据的行数变了。



### 3.4.3 四大隔离级别

|            隔离级别            |  脏读  | 不可重复读 |  幻读  | 一致性读实现             |
| :----------------------------: | :----: | :--------: | :----: | ------------------------ |
| Read Uncommitted<br />读未提交 |  可能  |    可能    |  可能  | 直接读取版本的最新记录   |
|  Read Committed<br />读已提交  | 不可能 |    可能    |  可能  | 使用版本链实现(ReadView) |
| Repeatable Read<br />可重复读  | 不可能 |   不可能   |  可能  | 使用版本链实现(ReadView) |
|    Serializble<br />串行化     | 不可能 |   不可能   | 不可能 | 通过加锁访问数据的实现   |

大多数数据库系统中，默认的隔离级别是读已提交(如Oracle)或可重复读。

InnoDB默认的隔离级别是RR。<font color='red'>需要注意的是，在SQL标准中，RR是无法避免幻读问题的，但是InnoDB实现的RR避免了幻读问题。</font>RR实现的核心机制，是基于MVCC机制来实现的。



### 3.5 MVCC

Muti-Version Concurrency Control，即多版本的并发控制协议。实现是通过保存数据在某一个时间点的快照，因此每一个事务无论执行多长时间，看到的数据，都是一样的。

它的实现依赖于 隐式字段、undo日志、快照读&当前读、Read View。

#### 3.5.1 隐式字段

对于InnoDB，每一行记录都会有两个隐藏列 DB_TRX_ID、DB_ROLL_PTR，如果表中没有主键和非NULL唯一键时，则还会有第三个隐藏的主键列 DB_ROW_ID。

- DB_TRX_ID：记录每一行最近一次修改(修改/更新)它的事务ID。
- DB_ROLL_PTR：这个隐藏列就相当于一个指针，指向回滚段的undo日志，通过指针找到之前版本，通过链表形式组织。
- DB_ROW_ID：单调递增的行ID。



<a href='#undo'>undo日志</a>



### 3.5.2 快照读&当前读

- 快照读：读取的是记录数据的可见版本(有旧的版本)，不加锁，普通的select语句都是快照读。
- 当前读：读取的是记录数据的最先版本，显示加锁的都是当前读。



### 3.5.3 ReadView

>Read view lists the trx ids of those transactions for which a consistent read should not see the modifications to the database.



- 通过隐藏列和版本链，MySQL可以将数据恢复到指定版本；但是具体要恢复到哪个版本，则需要根据ReadView来确定。

- ReadView就是事务执行快照读时，产生的读视图。
- 事务执行快照读时，会产生数据库系统当前的一个快照(trx_sys)，记录当前系统中还有哪些活跃的读写事务，把他们放到一个列表里。
- ReadView主要是用来做可见性判断的，即判断当前事务可见哪个版本的数据。

<font color='red'>ReadView是与SQL绑定的，并不是事务，每次SQL启动时构造ReadView的up_limit_id和low_limit_id页都是不一样的。</font>



#### 3.5.3.1 ReadView组成

> up_limit_id：
> The read should see all trx ids which are strictly smaller (<) than this value.
> In other words, this is the low water mark".
>
> low_limit_id：
> The read should not see any transaction with trx id >= this value.
> In other words, this is the "high water mark".
>
> m_ids：
> Set of RW transactions that was active when this snapshot was taken.

- up_limit_id：最先开始的事务，该SQL启动时，当前事务链表中最小的事务id编号，也就是当前系统中创建最早但还未提交的事务。
- low_limit_id：最后开始的事务，该SQL启动时，当前事务链表中最大事务id编号，也就是最近创建的除自身以外最大事务编号。
- m_ids：当前活跃事务id列表，所有事务链表中事务id集合。

**id越小，事务开始的越早；id越大，事务开始的越晚**



#### 3.5.3.2 可见性判断

- 如果读取出来的数据行上的db_trx_id小于up_limit_id，则说明这条记录的最后修改在ReadView创建之前，因此这条记录可以被看见。
- 如果读取出来的数据行上的db_trx_id大于low_limit_id，则说明这条记录的最后修改在ReadView创建之后，因此这条记录肯定不可以被看见。
- 如果读取出来的数据行上的db_trx_id在low_limit_id和up_limit_id之间，则查找该数据上的db_trx_id是否在ReadView的m_ids中
  - 如果存在，则表示这条记录的最后修改是在ReadView创建之时，被另外一个活跃事务所修改，所以这条记录也不可以被看见。
  - 如果不存在，则表示这条记录的最后修改在ReadView创建之前，所以可以看到。



**RR和RC最大的区别就是：RC每次读取数据前都生成一个ReadView，而RR只在第一次读取数据时生成一个ReadView。**



# 4 日志

由于磁盘随机读写的效率很低，MySQL为了提高性能，读写不是直接操作的磁盘文件，而是在内存中开辟了一个叫做buffer pool的缓存区域，更新数据的时候会优先更新到buffer pool，之后再由I/O线程写入磁盘。同时InnoDB为了保证当即不丢失buffer pool中的数据，实现crash safe，还引入了一个叫做redo log的日志模块。另外还有处于MySQL Server层的用于备份磁盘数据的bin log，用于事务回滚和MVCC的undo log等。

## 4.1 buffer pool

buffer pool作为了一个缓冲池，以页为单位，用于缓存数据和索引等数据，对应表空间中的页。回到MySQL组件图，一条SQL经过服务层各个组件的处理之后，最终通过执行器调用存储引擎提供的接口执行。如果是要更新一条数据，那么会先找到数据所在页，将该页加载到buffer pool中，在buffer pool中对数据进行修改，最终会通过IO线程再以页为单位将缓存中的数据刷入磁盘。



## 4.2 <span id='redo'>redo log</span>

由于引入了buffer pool，数据不是实时写入磁盘的，如果数据还没有写入磁盘的时候MySQL宕机了，那么缓存中的数据不就丢失了吗？使用redo log来记录这些操作，即使MySQL宕机，那么在重新启动后也能根据这些记录来回复还没来得及写入磁盘的数据，进而保证了事务的持久性。redo log是物理日志，记录了某个数据页上做了什么修改，属于InnoDB引擎，MyISAM等不具备。

记录会先在buffer pool中更新，当pool中更新之后会在redo log buffer中添加对应的记录，记录某个数据页上做了什么修改，事务会被设置为prepare状态，这个时候就可以开始根据策略刷盘了，然后等待Server层处理(比如binlog写入)，在事务提交之后，标识redo log为已提交。

redo log buffer中的数据也不是直接入盘，中间还会经过操作系统内核空间的缓冲区(os buffer)，然后才到磁盘上的redo log file。`innodb_flush_log_at_trx_commit`参数可以控制redo log buffer何时写入redo log file，该参数有三个可选值

- 0：延迟写。不会在事务提交时立即将redo log buffer写入到os buffer，而是每秒写入os buffer，然后立即写入到redo log file，也就是每秒刷盘。
- 1：实时写，实时刷：每次事务提交都会将redo log buffer写入os buffer，然后立即写入redo log file。数据能够及时入盘，但是每次事务提交都会刷盘，效率较低。
- 2：实时写，实时刷。每次事务提交豆浆redo log buffer写入os buffer，然后每秒将os buffer写入到redo log file。

buffer pool中的数据需要刷盘，redo log buffer中的数据页也需要刷盘。如果事务提交成功之后buffer pool中的数据还没有刷盘，这是MySQL宕机了，那么在重启时通过比对redo log file和数据页，可以从redo log file中恢复数据，redo log file根据innodb_flush_log_at_trx_commit参数配置，通常最多丢失一秒的数据。



## 4.3 <span id='undo'>undo log</span>

- 事务未提交的时候，修改数据的镜像(修改前的数据)，存到undo日志里。一遍事务回滚时，恢复旧版本数据，撤销未提交事务数据对数据库的影响。
- undo日志是逻辑日志。可以这样认为，当delete一条记录时，undo log中会记录一条对应的insert记录，当update一条记录时，它记录一条对应相反的update记录。
- 存储undo日志的地方，就是回滚段。

多个事务并行操作某一行数据时，不同事务对该行数据的修改会产生多个版本，然后通过回滚指针(DB_ROLL_PTR)连成一条Undo日志链。

操作过程如下：

1. 将待操作的行加排他锁。
2. 将该行远门的值拷贝到undo log中，db_trx_id和db_roll_ptr保持不变(形成历史版本)。
3. 修改该行的值，更新该行的db_trx_id为当前操作事务的事务id，将db_roll_ptr指向第二步拷贝到undo log链中的旧版本记录。(通过db_roll_ptr可以找到历史记录)
4. 记录redo log，包括undo log中的修改。



在InnoDB里，undo log分为两种类型

- insert undo log：插入产生的undo log。不需要维护历史版本链，因为没有历史数据，所以其产生的undo log可以在事务提交之后删除，不需要purge操作。
- undate undo log：更新或删除产生的undo log。不会在提交后就立即删除，而是会放入undo log历史版本链，用于MVCC，最后由purge线程清理。



## 



# 5 SQL优化

加索引

避免返回不必要的数据

适当分批量进行

优化sql结构

分库分表

读写分离

[后端程序员必备：书写高质量SQL的30条建议](https://juejin.cn/post/6844904098999828488)



# 参考资料

- [社招后端21连问（三年工作经验一面)](https://mp.weixin.qq.com/s/zYaleLjjpp8wfHs23eVuKg)
- [MySQL面试经典100题（收藏版，附答案）](https://www.cnblogs.com/setalone/p/14851000.html)
- [MySQL 的覆盖索引与回表](https://learnku.com/articles/40421)
- [五分钟搞懂MySQL索引下推 ](https://www.cnblogs.com/three-fighter/p/15246577.html)
- [再有人问你为什么MySQL用B+树做索引，就把这篇文章发给她](https://mp.weixin.qq.com/s?__biz=Mzg3NzU5NTIwNg==&mid=2247487988&idx=1&sn=eccbb31faa4f580ae71fbea5cd4ff01b&source=41#wechat_redirect)
- [一文彻底读懂MySQL事务的四大隔离级别](https://juejin.cn/post/6844904115353436174#heading-8)
- [什么是MySQL MVCC的ReadView？](https://www.modb.pro/db/75331)
- [MySQL--buffer pool、redo log、undo log、binlog](https://blog.csdn.net/huangzhilin2015/article/details/115396599)
