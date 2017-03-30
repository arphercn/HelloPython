1 搭建开发环境  
    
	start study flask on www.liaoxuefeng.com by a instance of a blog

2 编写Web App骨架

    2.1 线程threading:一个线程就是执行一个子程序  
    2.2 生成器generator:  
        如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的
        过程中不断推算出后续的元素呢
        可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generato
    2.3 协程coroutine:  
        一个子程序中中断，去执行其他子程序. 子程序就是协程的一种特例
        因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，
			既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
        Python对协程的支持是通过generator实现的。
    2.4 asyncio:  
        多个coroutine就可以由一个线程并发执行
        比如,两个hello world程序由一个线程并发执行
