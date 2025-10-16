### Threads

#### When we need multiple threads to keep good user response
+ gui-io.py: without threads, the GUI frozen!
+ gui-io-threads.py: with threads, the GUI keeps responsive!

#### Inspect the threads in Linux
+ check the threads states when they are running:
    ```bash
    ps -Lo pid,lwp,stat,cmd -p pid
    ```
    the outout could be:
    ```shell
    PID     LWP STAT CMD
    1191    1191 Sl   python3 gui-io-threads.py
    1191    1192 Sl   python3 gui-io-threads.py
    ```
+ runtime resources usage:
    ```bash
    top -Hp pid
    ```
+ check the TCB (thread control block) in Linux 
    ```shell
    cat /proc/<pid>/task/<tid>/status
    ```
    1 to 1 implementation: 1 user level thread (ULT) corresponds to 1 kernel support thread (KST)