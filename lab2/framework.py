from threading import Thread, Lock, Condition, Semaphore
from typing import Any, List

class BoundedBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: List[Any] = []
        
    def put(self, item: Any):
        self.buffer.append(item)

    def get(self) -> Any:
        item = self.buffer.pop(0)
        return item
    
class BoundedBufferBasic:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.buffer: List[Any] = []
        
    def put(self, item: Any):
        raise NotImplementedError

    def get(self) -> Any:
        raise NotImplementedError

class BoundedBufferCV:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: List[Any] = []
        
    def put(self, item: Any):
        raise NotImplementedError

    def get(self) -> Any:
        raise NotImplementedError

class BoundedBufferCV2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: List[Any] = []
        
    def put(self, item: Any):
        raise NotImplementedError

    def get(self) -> Any:
        raise NotImplementedError


class BoundedBufferSem:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer: List[Any] = []
        
    def put(self, item: Any):
        raise NotImplementedError

    def get(self) -> Any:
        raise NotImplementedError


def demo():
    bb = BoundedBuffer(5)

    def producer(i):
        pass

    def consumer():
        pass

    threads = []
    
    threads.append(Thread(target=producer, args=(1,)))
    threads.append(Thread(target=consumer))

    [t.start() for t in threads]
    
    [t.join() for t in threads]
    
    # assert num_consumed == num_produced

if __name__ == "__main__":
    # 给定生产/消费线程数, 每个线程生产/消费的item数, 计算demo耗时
    demo()
