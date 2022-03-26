
## Process(进程)

一个程序至少有一个进程，一个进程至少有一个线程。
进程就是一个应用程序在处理机上的一次执行过程，它是一个动态的概念。

多进程中，不同的子进程的进程号不同。



## Thread(线程)
线程是进程中的一部分，进程包括多个线程在运行。

进程的子任务称为线程。

多线程中，所有的子线程的进程号相同。

### Mutex(线程锁)

多线程程序涉及到一个问题，就是当不同线程要对同一个资源进行修改或利用时会出现混乱，所以有必要引入线程锁。
要注意创建线程也是需要时间的。
线程锁也称互斥锁，可以弥补部分线程安全问题。
当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制。
线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制就是引入互斥锁。
互斥锁为资源引入一个状态：锁定/非锁定。
某个线程要更改共享数据时，先将其锁定，此时资源的状态为锁定，其他线程不能更改；直到该线程释放资源，将资源的状态变为非锁定，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。


## Coroutine(协程)


## Parallel(并行)

是计算机系统中能同时执行两个或更多个处理的一种计算方法。并行处理可以同时工作于同一个程序的不同方面。并行处理的主要目的是节省大型和复杂问题的解决时间。


## Concurrent(并发)

指一个时间段中有几个程序都处于已启动运行到运行完毕之间，且这几个程序都是在同一个处理机(CPU)上运行，但任意时刻点上只能有一个程序在处理机上运行。

## Synchronous(同步)

指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，直到收到返回信息才会继续执行下去。

## Asynchronouss(异步)

指线程不需要一直等待下去，而是继续执行下面的操作，不管其他进程的状态，当有消息返回时系统会通知进程进行处理，这样可以提高执行效率。


## CPU-bound(计算密集型)

就是应用非常多的CPU计算资源，计算密集型任务的特点是要进行大量的计算，消耗CPU资源。

## IO-bound(IO密集型)

对于IO密集型的应用，涉及到网络、磁盘IO的任务都是IO密集型任务，大多消耗都是硬盘读写和网络传输的消耗。

# 参考资料

- [进程与线程的一个简单解释](http://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html)
- [一文读懂什么是进程、线程、协程（建议收藏）](https://www.1024sou.com/article/108689.html)
