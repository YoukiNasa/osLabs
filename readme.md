### Codes used in my Operating System class

The source files are organized into folders `c[x]` by chapters and `lab[x]` by Labs.

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
    compile and then run multiples and check/kill the process:
    ```bash
    gcc 1_cpu.c -o cpu.o
    ./cpu A & ./cpu.o B &
    ps aux | grep cpu
    kill [pid]
    ```
+ `2_mthreads.c`: show that without OS, concurrency will bring mistakes.

#### lab1
+ `templates.md`: template for writing the report of the Lab1 assignment. 
+ `students_v1.csv` and `students_v2.csv` for comparison.
+ `c_project`: for file processing jobs.
+ `linux.png`: for image processing jobs.


