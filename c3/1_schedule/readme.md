### Schedule

+ `analyser.py`: calculate the metrics like turnaround time, response time, waiting time, throughput...

#### job schedule (long-term)
+ `job_schedule.py`: simulating the job schedule algorithms that is **non-preemptive**
  + FCFS: first come first serve
  + SJF: shortest job first
  + priority: high priority first
  + HRRN: Highest Response Ratio Next
+ `job_schedule_preemptive.py`:simulating the job schedule algorithms that is **preemptive**
  + SRTF: smallest remaining time
  + PRIO_P: effective priority with linear aging (smaller is better)
  + HRRN_P: Highest Response Ratio using remaining time

#### process schedule (short-term)
+ `process_schedule.py`: simulating process schedule algorithms:
  + RR: Round Robin
  ```py
  process = [Process("P0",0,5), Process("P1",1,3), Process("P2",2,4)]
  gantt = simulate_rr(process, quantum=2)
  arrivals = {j.name:j.arrive for j in process}
  total = sum(j.svc for j in process)
  m, per = metrics_gantt(gantt, arrivals, total)
  plot_gantt(gantt, "Round Robin Scheduling (quantum=2)")
  ```
  + MLFQ: Multi-level feedback queue
  ```py
  process = [Process("P0",0,3), Process("P1",1,3), Process("P2",2,4)]
  gantt = simulate_mlfq(process,(1,2))
  arrivals = {j.name:j.arrive for j in process}
  total = sum(j.svc for j in process)
  m, per = metrics_gantt(gantt, arrivals, total)
  plot_gantt(gantt, "Multi-level feedback queue (quantum=1,2)")
  ```

#### real-time schedule (driven by deadline)
+ `realtime_schedule.py`: simulating real-time scheduler:
  + EDF: earliest deadline first.
  + LST/LLF: least slack / least laxity first