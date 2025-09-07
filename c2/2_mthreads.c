#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

int balance = 1000;

void* deposit(void *arg) {
    int amount = *(int*)arg;
    for(int i=0; i<5; i++){
        usleep(1000);
        int current_balance = balance;
        usleep(1000);
        balance = current_balance + amount;
        printf("Deposit: +%d, balance: %d\n",amount,balance);
    }
}

void* withdraw(void *arg) {
    int amount = *(int*)arg;
    for(int i=0; i<5; i++){
        usleep(1000);
        int current_balance = balance;
        usleep(1000);
        balance = current_balance - amount;
        printf("Withdraw:-%d, balance: %d\n",amount,balance);
    }
}

int main(){
    pthread_t deposit_t, withdraw_t;
    int deposit_amount = 100;
    int withdraw_amount = 50;
    printf("initial balance = %d\n", balance);

    pthread_create(&deposit_t, NULL, deposit, &deposit_amount);
    pthread_create(&withdraw_t, NULL, withdraw, &withdraw_amount);

    pthread_join(deposit_t, NULL);
    pthread_join(withdraw_t, NULL);

    printf("Final Balance: %d\n", balance);

    return 0;
}
