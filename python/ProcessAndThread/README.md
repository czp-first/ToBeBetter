

[process and thread in os](https://github.com/czp-first/ToBeBetter/tree/master/operating_system/ProcessAndThread)

# GIL(Global Interpreter Lock)
GIL是CPython引入的一个概念。

GIL并不是Python的特性，Python完全可以不依赖于GIL。

Python中由于GIL的存在，在多线程时并没有真正的进行多线程计算。GIL说白了就是伪多线程，一个线程运行时其他线程阻塞，使得多线程代码不是同时执行，而是交替执行。

多线程可能反而会更慢，原因可以参考pcode数量的调度方式。

GIL多线程的不足，其实是对计算密集型的不足，这个解决可以利用多进程进行解决，而对于IO密集型任务，还是可以使用多线程进行提升效率。

[Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock)(全局解释器锁)