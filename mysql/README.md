<div align='center'><img src='https://github.com/czp-first/ToBeBetter/blob/master/icons/mysql.svg'></div>

# 索引

## 索引类型

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



## B-树与B+树的区别

- B-树内部节点是保存数据的；而B+树内部节点是不保存数据的，只起索引作用，它的叶子节点才保存数据
- B+树相邻的叶子节点之间是通过链表指针连起来的，B-树却不是
- 查找过程中，B-树在找到具体的数值以后就结束，而B+树可以出现多次



## 为什么索引结构默认使用B+树，而不是B-Tree、Hash、二叉树、红黑树？

- Hash，只适合等值查询，不适合范围查询
- 一般二叉树，可能会特殊化为一个链表，相当于全表扫描
- 红黑树，是一种特化的平衡二叉树，MySQL数据量很大的时候，索引的体积也会很大，内存放不下的而从磁盘读取，树的层次太高的话，读取磁盘的次数就多了
- B-Tree，叶子节点和非叶子节点都保存数据，相同的数据量，B+树更矮壮，也就是说，相同的数据量，B+树数据结构，查询磁盘的次数会更少



## mysql索引在什么情况下会失效

- 查询条件包括or，可能导致索引失效
- ？？？如果字段类型是字符串，where时一定用引号括起来，否则索引失效
- like通配符可能导致索引失效
- 联合索引，查询时的条件列不是联合索引中的第一个列，索引失效
- 在索引列上使用mysql的内置函数，索引失效
- 在索引列运算（如：+、-、*、\），索引失效
- 索引字段上使用（!= 、<>、not in）时，可能导致索引失效
- 索引字段上使用is null，is not null，可能导致索引失效
- 左连接查询或者右连接查询，查询关联的字段编码格式不一样，可能导致索引失效。
- mysql估计使用全表扫描要比使用索引快，则不使用索引



# 存储引擎

## mysql的存储引擎InnoDB与MyISAM的区别

- InnoDB支持事务，MyISAM不支持事务
- InnoDB支持外键，MyISAM不支持外键
- InnoDB支持MVCC（多版本并发控制），MyISAM不支持
- select count(*) from table时，MyISAM更快，因为它有一个变量保存了整个表的总行数，可以直接读取，InnoDB就需要全表扫描
- InnoDB不支持全文索引，而MyISAM支持全文索引（5.7以后的InnoDB也支持全文索引）
- InnoDB支持表、行级锁，而MyISAM支持表级锁
- InnoDB表需要更多的内存和存储，而MyISAM可被压缩，存储空间较小
- InnoDB按主键大小有序插入，MyISAM记录插入顺序时，按记录插入顺序保存
- InnoDB存储引擎提供了具有提交、回滚、崩溃恢复能力的事务安全，与MyISAM比，InnoDB写的效率差一些，并且会占用更多的磁盘空间以保留数据和索引





# 参考资料

- [社招后端21连问（三年工作经验一面)](https://mp.weixin.qq.com/s/zYaleLjjpp8wfHs23eVuKg)
- [MySQL面试经典100题（收藏版，附答案）](https://www.cnblogs.com/setalone/p/14851000.html)

