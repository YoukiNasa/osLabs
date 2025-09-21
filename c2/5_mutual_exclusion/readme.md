### Concurrency - Mutual Exclusion

To run the programs, compile them use gcc:
```shell
gcc name.c -o name.o -lpthread && ./name.o
```

+ `sum.c`: a simple multi-threads program summing a **critical resource** `sum` via their **critical section**: `sum++;`
  
+ `sum_lock.c`: use a simple lock. This will fail as the load/store command is not **atomic** (i.e., hardware primitives)
  
+ `sum_peterson.c`: a non-atomic implementation of [Peterson algorithm](https://zoo.cs.yale.edu/classes/cs323/doc/Peterson.pdf), so will also fail, but is better compared with naive lock.
  
+ `sum_peterson_atomic_seq_cst.c`: a atomic and sequential consistent implementation of Peterson Algorithm using [`stdatomic.h`](https://en.cppreference.com/w/cpp/header/stdatomic.h). This will solve the mutual exclusion problem.

+ `sum_mutex.c`: solving ME by `mutex` provided by `pthread.h`. Actually this is `spintex (based on xchg primitive) + mutex = futex`.

+ \* `sum_semaphore.c`: solving ME by **semaphore**. (see also `6_sync/`)

One can compare the methods of *atomic peterson* and *mutex*:

```bash
echo "peterson:" && time ./sum_peterson_atomic_seq_cst.o && echo "mutex:" && time ./sum_mutex.o
```

The output could be:
```
peterson:
sum is 2000000

real    0m0.248s
user    0m0.492s
sys     0m0.000s
mutex:
sum is 2000000

real    0m0.105s
user    0m0.129s
sys     0m0.073s
```

you will find that Peterson will not enter the `system kernel` ($sys=0$) but it is not as efficient as mutex ($real=0.248 > 0.105$).