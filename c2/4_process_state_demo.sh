#!/bin/bash

#!/usr/bin/env bash
set -euo pipefail

show_state() {
  local pid="$1"
  echo "pid=$pid"
  ps -o pid,ppid,state,cmd -p "$pid"
}

# 1) Create a SLEEPING process (state S)
sleep 1000 &
SLEEP_PID=$!
echo "Started: sleep 1000 (pid=$SLEEP_PID)"
sleep 0.5
show_state "$SLEEP_PID"

# 2) STOP it with SIGSTOP (state T), then CONT it back to S
kill -STOP "$SLEEP_PID"
sleep 0.3
echo "After STOP:"
show_state "$SLEEP_PID"

kill -CONT "$SLEEP_PID"
sleep 0.3
echo "After CONT:"
show_state "$SLEEP_PID"

# 3) Create a short RUNNING/READY load (state R shows fleetingly)
yes > /dev/null &
YES_PID=$!
sleep 0.5
echo "Hint: 'R' is often momentary; use top/htop to catch it live."
show_state "$YES_PID"
# Keep it running a bit, then stop it so we can observe state change
kill -STOP "$YES_PID"
sleep 0.2
echo "After STOP (T):"
show_state "$YES_PID"
kill -CONT "$YES_PID"
sleep 0.2

# 4) Demonstrate a ZOMBIE (Z) with a short Python forker
# Parent sleeps without wait(); child exits immediately => child becomes zombie.
# Keep parent around long enough to observe the zombie.
python3 - <<'PY' &
import os, time, sys, signal
pid = os.fork()
if pid == 0:
    # Child exits immediately -> becomes zombie until parent waits or exits
    sys.exit(0)
else:
    # Parent sleeps (does NOT wait) so child stays zombie for ~20s
    time.sleep(20)
PY
PARENT_PY=$!
sleep 0.4

# Find the (recent) child of the Python parent (likely in Z state)
echo "Looking for zombie child of parent $PARENT_PY ..."
ps -o pid,ppid,state,cmd --ppid "$PARENT_PY" | (read; cat) || true

# 5) Termination: SIGTERM vs SIGKILL and cleanup
echo "Terminating 'yes' (pid=$YES_PID) with SIGTERM..."
kill -TERM "$YES_PID" || true
sleep 0.2
show_state "$YES_PID" || echo "(yes terminated)"

echo "Terminating 'sleep' (pid=$SLEEP_PID) with SIGKILL..."
kill -KILL "$SLEEP_PID" || true
sleep 0.2
show_state "$SLEEP_PID" || echo "(sleep terminated)"

# 6) uninterruptible sleep (Disk)
echo "example of (statue D) with sync file"
echo "NOTE: D is kernel-waiting (I/O), hard to reproduce reliably on healthy laptops."
echo "The following command may/may not show D state"
dd if=/dev/zero of=/tmp/bigfile bs=16M oflag=sync count=64 &
sleep 0.4
show_state $! || true

