#include <sys/shm.h>
#include <stdio.h>

int main() {
    int shmid = shmget(IPC_PRIVATE, 1024, IPC_CREAT | 0666);
    
    char *shared_memory = (char*)shmat(shmid, NULL, 0);
    
    sprintf(shared_memory, "Hello from Process 1!");
    
    printf("Process 2 received: %s\n", shared_memory);
    
    shmdt(shared_memory);

    shmctl(shmid, IPC_RMID, NULL);
    return 0;
}