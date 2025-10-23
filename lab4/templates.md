### 实验4：进程调度
*OS2025-2026 信计231 Name[ID]*

#### 调度算法的实现与运行结果
（给出**至少2种**调度算法的实现，实验报告中列出关键代码，并给出运行结果）
##### 轮转调度算法 RR
+ 实现
  ```py
  # 给出核心代码
  ```
+ 运行结果
  (需要看到明显的进程切换，并且保证每个进程运行正确, 比如我有两个进程，一个打印斐波那契数列`Fibonacci.asm`，一个是计算1+2+..+5,打印最终结果`Addition.asm`,可能的输出是：)
  ```
    Starting Fibonacci(1)
    PRINT: 1
    PRINT: 2
    Switching from Fibonacci(1) to Addition(2)
    Switching from Addition(2) to Fibonacci(1)
    PRINT: 3
    PRINT: 5
    Switching from Fibonacci(1) to Addition(2)
    Switching from Addition(2) to Fibonacci(1)
    PRINT: 8
    Switching from Fibonacci(1) to Addition(2)
    PRINT: 15
    Process Addition(2) completed.
    Starting Fibonacci(1)
    PRINT: 13
    PRINT: 21
    PRINT: 34
    PRINT: 55
    PRINT: 89
    Process Fibonacci(1) completed.
    No process in ready queue.
    No process to schedule. CPU idle.  
  ```

#### 思考与讨论
1. 请比较你所实现的调度算法的优劣和适宜的应用场景。


2. 通过本次实验，谈一谈你对进程切换的新的理解，进程切换的开销体现在哪些方面？ 

  
  