### 实验3：CPU/内存模拟与程序执行
#### 实验目的
1. 理解CPU和内存运行的原理
2. 理解机器指令与汇编，理解程序执行的特点
3. 实现简单PCB和操作系统，为进程调度实验做准备

#### 1. CPU & Memory
```python
class CPU:
    def __init__(self):
       self.pc 
       self.memory
       self.register
```
CPU就是一个无情的 **加载指令，执行指令**的机器
```python
class CPU:
    def run(self):
        while True:
            self.fetch() # 加载指令
            self.execute() # 执行指令
    
    def fetch(self):
        pass
    
    def execute():
        pass
```

+ 程序指针 PC: Program Counter
  ```python
  class ProgramCounter:
    def __init__(self):
        self.value = 0
    def inc(self):
        self.value += 1
    def reset(self):
        self.value = 0
    def set_value(self, value):
        self.value = value
  ```
+ 寄存器Register：
  ```python
    self.registers = {
        'ACC': 0,  # Accumulator
        'FLAGS': 0, # Flags Register
    }
  ```
+ 内存：连续存储空间，无堆栈（所以，无法实现函数调用）
  ```python
  # self -> CPU
  self.memory = [0] * self.memory_size
  ```
+ ALU(算数逻辑单元) $\to$ 指令集：自定义机器指令
  ```python
  # self -> CPU
  self.instruction_set = {
    0x01: self._load, # Load TO ACC
    0x02: self._add, # add ACC
    ...
  }

  def _load(self):
    addr = self.memory[self.pc.value]
    self.pc.inc()
    self.registers['ACC'] = self.memory[addr]

  def _add(self):
    addr = self.memory[self.pc.value]
    self.pc.inc()
    self.registers['ACC'] += self.memory[addr]
    ...
  ```

#### 2. Machine Language & Assembler
```asm
; calculate a+b
LOAD a
ADD b
a:2
b:3
```
运算结果需使得CPU的ACC寄存器：`ACC = 2 + 3 = 5`

1. 文本处理：去除空格和注释
2. 代码解析：区分label, var和指令
3. 根据指令生成机器码，内存地址转换

请参考`asm.py`中的是实现，并用`add.asm`测试：
```shell
python3 asm.py add.asm
```

#### 3. Simple OS
创建进程，修改进程状态，加载程序至内存，控制CPU执行等：
```python
class OperatingSystem:
    def __init__(self):
        self.cpu = CPU()
        self.process = []
        self.next_pid = 1
        self.ready_queue = []
        self.clock = 0

    def create_process(self, program, name="Process"):
        # create a new process and add to the process list
        # like linux's fork()
        pass
        self.ready_queue.append(PCB(self.next_pid, name, program))
        
    def load_program(self, process:PCB):
        # load the program into memory
        pass

    def run(self):
        pass
```
#### 4. Assignment
+ 以`framework/`中的代码为基础进行开发，编写汇编实现斐波那契数的保存：
  + TIPS: 需要用到循环，所以要实现**跳转指令**，并注意使用程序计数器PC的`set(value)`方法
  + 修改`asm.py`文件：添加新的指令
  + 修改`cpu.py`文件：添加新的机器指令`xxx`并实现`self._xxx(self)`，需要和`asm.py`中的对应，在`pass`处实现方法对应的功能
  + 修改`pyos.py`文件：添加必要的代码，并在`pass`处实现方法对应的功能
+ 提交一个压缩包`OS_Lab3_name.zip`，内容包括：修改后的`asm.py`,`cpu.py`,`pyos.py`以及一个汇编文件`fibonacci.asm`实现在内存中保存斐波那契数字；
+ **deadline: By the Friday of Week 8 (2025/10/24).**
+ submit to: xsun@gzhu.edu.cn, subject(邮件主题): Assignment-OS-Lab3