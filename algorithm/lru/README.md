# LRU(least recently used)



## 标准LRU

1. 新增key/value的时候首先在链表结尾添加Node节点, 如果超过LRU设置的阈值就淘汰队头的节点并删掉HahsMap中对应的节点。
2. 修改key对应的值的时候先修改对应的Node中的值, 然后把Node节点移动到队尾。
3. 访问key对应的值的时候把访问的Node节点移动到队尾即可。



## Redis近似LRU

在redis的dict中每次按key获取一个值时，都会调用lookupkey函数，如果配置了LRU模式，该函数会更新value(robj)中的lru字段未当前秒级别的时间戳。虽然记录了每个value的时间戳，但是淘汰时总不能挨个遍历dict中的所有槽，逐个比较lru大小吧。

redis初始的实现算法，随机从dict中取出5个key，淘汰一个lru字段值最小的。随机选取的key是个可配置的参数maxmemory-samples，默认值为5。

3.0时改进了一版算法，首先第一次随机选取的key都会放入一个pool中(pool的大小为6)，pool中的key是按lru大小顺序排列的。接下来每次随机选取的key的lru值必须小于最小的才会继续放入，直到将pool放满。放满之后，每次如果有新的key需要放入，需要将pool中lru最大的一个key取出。

淘汰的时候，直接从pool中选取一个lru最小的值然后将其淘汰