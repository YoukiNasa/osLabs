### 实验2：进程的互斥与同步

#### 有限缓冲区-BoundedBuffer
1. 用python实现一个boundedBuffer类，需要具有以下的功能：
```python
class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        pass
    
    def put(self, item):
        pass

    def get(self):
        pass
```
+ 缓冲区大小：`capacity`
+ `put`操作：当缓冲区不满时，向缓冲区存入数据
+ `get`操作：当缓冲区非空时，从缓冲区读走数据

2. 错误的实现，没有任何互斥与同步机制的保证：
```python
class BoundedBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: List[Any] = []
        
    def put(self, item: Any):
        self.buffer.append(item)

    def get(self) -> Any:
        item = self.buffer.pop(0)
        return item
```
3. 不一定正确, 但是一定低效的实现:
   + 使用`count`变量: `put`就+1,`get`就-1,然后每次访问判断`count`是否满足某个条件.

4. 正确的实现方式
   + 使用1个锁 + 2个条件变量:`threading.Lock`,`threading.Condition`
   + 使用1个锁 + 1个条件变量
   + 使用信号量:`threading.Semaphore`

#### 多线程（对无OS的多进程模拟）
+ 创建多个生产者（执行`put`）和消费者（执行`get`）线程.
+ 可以指定生产和消费的数据数量，比较不同实现方式的效率.
```python
bb = BoundedBuffer(5)
produced = []
consumed = []

def producer(i):
    while len(produced) < N:
        x = (i, random.randint(1,100))
        bb.put(x); produced.append(x)

def consumer(i):
    while len(consumed) < N:
        x = bb.get(); consumed.append(x)

threads = []
for i in range(n):
    threads.append(Thread(target=producer, args=(i,)))
    threads.append(Thread(target=consumer, args=(i,)))
```
+ 可以使用asset检测结果是否正确:
```python
assert len(consumed) <= len(produced)
print("Produced:", len(produced), "Consumed:", len(consumed))
```

#### Assignment
+ format: `.py`, `.md`, and `.pdf`
+ submitted file name: `0S_Lab2_name.py`,`0S_Lab2_name.md` and `0S_Lab2_name.pdf`
+ **deadline: By the Friday of Week 6 (2025/10/10).**
+ submit to: xsun@gzhu.edu.cn, subject: Assignment-OS-Lab2