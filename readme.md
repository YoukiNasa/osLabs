#### Codes used in my Operating System class

The source files are organized into folders `c[x]` by chapters.

##### c1
+ `1_hello.c`: show how computer could read binary while we coding in C
  ```bash
  gcc 1_hello.c -o 1_hello.o
  ```
  then use `xdd` to say the binary file:
  ```bash
  xdd 1_hello.o | less
  ```

#### c2
+ `1_concurrency_cpu.c`: show OS makes concurrency possible.
    compile and then run multiples and check the process:
    ```bash
    gcc 1_cpu.c -o 1_cpu.o
    ./cpu A & ./1_cpu.o B &
    ps aux | grep cpu
    ```
+ `2_mthreads.c`: show without OS, concurrency will bring mistakes.

