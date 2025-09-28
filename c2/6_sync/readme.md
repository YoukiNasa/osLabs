### Concurrency - Synchronization

To run the programs, compile them use gcc:
```shell
gcc name.c -o name.o -lpthread && ./name.o
```

+ `pro_con.c`: a example of producer_consumer problem, producers print `{` while consumers print `}`. This idea is adapted from [JYY](https://jyywiki.cn/index.html) of NJU. 

    ```C
    void* producer(void *args)
    {
        while(1)
        {
            printf("{");
        }
    }
    void* consumer(void *args)
    {
        while(1)
        {
            printf("}");
        }
    }
    ```
    A valid pattern with a given buffer `limit = 2` printed by this multiple threads program should be like `{{}}{}` , `{{}`, but is not `{{{}` (overflow), `{}}` (read NULL).
    To check part of the program's output：
    ```shell
    ./pro_con.o 2 2 3 | head -c 100
    ```
    or you can set a timeout for the program:
    ```bash
    timeout --signal=SIGTERM 0.1s ./pro_con.o 2 2 3
    ```

+ `check.py`: Python scripts for checking the validity of the pattern. 
  + check a string with `limit=2`:
  ```shell
  echo "{{}{}}" | python3 check.py 2
  ```
  + check a string with no buffer limit:
  ```shell
  echo "{{}{{}{{}}}}}" | python3 check.py
  ``` 
  + check the output of C program (need a tmp.txt to store the output, otherwise refer to `model_check.py`):
  ```shell
  ./pro_con_cv.o 1 1 5 | head -c 512 > text.txt && echo -e "\n" >> text.txt
  cat text.txt | python3 checker.py 5
  ```
+ `model_check.py`: check the program which continues printing the pattern, for example, check the output of the program with 2 producer, 2 consumer and buffer `limit=3`:
  ```shell
  ./pro_con.o 2 2 3 | python3 model_check.py 3
  ```  

+ `pro_con_mutex.c`: use **mutex** to solve producer-consumer, it works but is not efficient because it has spins (the process should always waked up to check the `count`).

+ `pro_con_cv.c`: use 1 **conditional variable** to solve producer_consumer problem, but it fails when there are more than 2 consumers/producers.

+ `pro_con_cv2.c`: update the implementation of **conditional variable**. It still does dot work because of **Spurious Wakeups**. So we should change `if` to `while` to guarantee that the condition is always meet.

+ `pro_con_cv_general.c`: a general way to use **mutex** and 1 **conditional variable** to solve the synchronization problem, i.e., `while(!condition)` and `broadcast(cv)`.

+ `pro_con_semaphore.c`: use **semaphore** to solve producer_consumer problem.

+ `philosopher_sem.c`: use **semaphore** to solve the Dinning Philosopher problem but will cause deadlock.
 
+ `philosopher_sem2.c`: use **semaphore** to solve the Dinning Philosopher problem with specific rules than can solve deadlock.
  
+ `philosopher_cv.c`: use **conditional variable** to solve the Dinning Philosopher problem, a easier way compared with effective **semaphore**.