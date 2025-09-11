#### Codes used in my Operating System class

The source files are organized into folders `c[x]` by chapters and 'lab[x]' for Labs.

#### Labs
Folders for files/materials used in the Labs
##### lab1
+ `templates.md`: tempalte for writing the report of the assignment. 
+ `students_v1` and `students_v2` for comparison.
+ `c_projects`: for file processing.
+ `linux.png`: for image processing.

#### c1
+ `1_hello.c`: show how computer could read binary while we coding in C
  ```bash
  gcc 1_hello.c -o 1_hello.o
  ```
  then use `xdd` to check the binary file:
  ```bash
  xdd 1_hello.o | less
  ```

#### c2
+ `1_cpu.c`: shows how OS makes concurrency possible.
    compile and then run multiples and check the process:
    ```bash
    gcc 1_cpu.c -o cpu.o
    ./cpu A & ./cpu.o B &
    ps aux | grep cpu
    ```
+ `2_mthreads.c`: show that without OS, concurrency will bring mistakes.

