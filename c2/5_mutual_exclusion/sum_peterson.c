#include<stdio.h>
#include<pthread.h>
#include<stdbool.h>
#include<unistd.h>

#define N 1000000
long sum = 0;

bool locked = false;
int flag[2] = {0};
int turn;

void *Tsum(void *arg) {
    int i = *(int *)arg;
    int j = 1 - i;
    for (int k = 0; k < N; k++){
       flag[i] = 1; //举旗
       turn = j;    //贴条
       while(flag[j] && turn==j);
       sum++; 
       flag[i] = 0;
    }
}

int main(){
    pthread_t tA, tB;
    int pA = 0, pB = 1;
    pthread_create(&tA, NULL, Tsum, &pA);
    pthread_create(&tB, NULL, Tsum, &pB);
    pthread_join(tA, NULL);
    pthread_join(tB, NULL);
    printf("sum is %ld\n", sum);
    return 0;
}

