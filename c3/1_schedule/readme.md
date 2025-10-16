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