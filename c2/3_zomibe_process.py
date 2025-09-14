import os,time,sys
pid = os.fork() # system call for creating process
if pid == 0:
    sys.exit(0)
else:
    time.sleep(20)
