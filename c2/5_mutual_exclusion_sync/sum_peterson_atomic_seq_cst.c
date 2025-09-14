#include <stdio.h>
#include <pthread.h>
#include <stdatomic.h>
#include <stdbool.h>
#include <sched.h>
#include <unistd.h>

#define N 1000000
static _Atomic bool flag[2];
static _Atomic int  turn;
static _Atomic long  sum = 0;

static void *Tsum(void *arg) {
    int i = *(int*)arg;
    int j = 1 - i;
    for (int k = 0; k < N; k++){
        atomic_store_explicit(&flag[i], true, memory_order_seq_cst); //flag[i] = 1
        atomic_store_explicit(&turn, j, memory_order_seq_cst); //turn = j
        while (atomic_load_explicit(&flag[j], memory_order_seq_cst) && 
                atomic_load_explicit(&turn, memory_order_seq_cst) == j) {
        };
        atomic_fetch_add_explicit(&sum, 1, memory_order_seq_cst); // sum++
        atomic_store_explicit(&flag[i], false, memory_order_seq_cst); // flag[i] = 0
    }
}

int main(void) {
    atomic_store(&flag[0], false);
    atomic_store(&flag[1], false);
    atomic_store(&turn, 0);
    pthread_t tA, tB;
    int p0 = 0, p1 = 1;
    pthread_create(&tA, NULL, Tsum, &p0);
    pthread_create(&tB, NULL, Tsum, &p1);
    pthread_join(tA, NULL);
    pthread_join(tB, NULL);
    printf("sum is %ld\n", sum);
}
