#include <sys/shm.h>
#include <stdio.h>

int main() {
    // 创建一个共享大小为1024，有读写权限的私有共享内存
    int shmid = shmget(IPC_PRIVATE, 1024, IPC_CREAT | 0666);
    
    // 获取共享内存的地址
    char *shared_memory = (char*)shmat(shmid, NULL, 0);
    
    sprintf(shared_memory, "Hello from Process 1!");
    
    printf("Process 2 received: %s\n", shared_memory);
    
    // detach from the process
    shmdt(shared_memory);

    // delete 
    shmctl(shmid, IPC_RMID, NULL);
    return 0;
}