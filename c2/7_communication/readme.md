### Process Communication
#### Types:
+ shared memory: we already accessed in synchronization
+ pipe: one-way, write->pipe->read
+ message passing
  + direct: send, receive
  + indirect: mailbox
+ client-server: socket, remote procedure call (RPC)

#### demos
+ `share_memory.c`: a simple C sample codes of shared memory via `sys/shm.h`.
+ `pipe_demo.py`: use Python to create a pipe between parent and child process.
+ `socket_demo.py`: use Python to test socket communication.
+ `message_passing.py` use `processing.queue` to realize multiple process communication. 