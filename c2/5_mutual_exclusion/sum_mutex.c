#include<stdio.h>
#include<pthread.h>

#define N 1000000
long sum = 0;

pthread_mutex_t sum_lock = PTHREAD_MUTEX_INITIALIZER;

void *Tsum(void *arg) {
    for (int i = 0; i < N; i++){
        pthread_mutex_lock(&sum_lock);
        sum++;
        pthread_mutex_unlock(&sum_lock);
    }
}

int main(){
    pthread_t tA, tB;
    pthread_create(&tA, NULL, Tsum, &sum);
    pthread_create(&tB, NULL, Tsum, &sum);
    pthread_join(tA, NULL);
    pthread_join(tB, NULL);
    printf("sum is %ld\n", sum);
}

