from typing import List, Tuple
from dataclasses import dataclass
import math
from analyser import metrics_gantt, plot_gantt

@dataclass
class RTJob:
    name: str
    arrive: int
    exec: int
    deadline: int

def simulate_rt(jobs, policy="EDF"):
    t=0; ready=[];
    pending=sorted(jobs,key=lambda x:x.arrive);
    rem={x.name:x.exec for x in jobs}; gantt=[]; finish={}
    def admit():
        nonlocal pending, ready, t
        while pending and pending[0].arrive<=t: ready.append(pending.pop(0))
    admit()
    while ready or pending:
        if not ready: t=pending[0].arrive; admit()
        if policy=="EDF": ready.sort(key=lambda x:x.deadline)
        elif policy=="LLF": ready.sort(key=lambda x:(x.deadline - (t + rem[x.name])))
        else: raise ValueError(f"Unknown policy: {policy}")
        cur=ready[0]; start=t; rem[cur.name]-=1; t+=1; admit()
        if rem[cur.name]==0: finish[cur.name]=t; ready.pop(0); gantt.append((cur.name,start,t))
        else: gantt.append((cur.name,start,t))
    collapsed=[]
    for n,s,e in gantt:
        if not collapsed: collapsed.append([n,s,e])
        else:
            if collapsed[-1][0]==n and collapsed[-1][2]==s: collapsed[-1][2]=e
            else: collapsed.append([n,s,e])
    gantt=[(n,s,e) for n,s,e in collapsed]
    
    miss = {j.name: (finish.get(j.name, math.inf) > j.deadline) for j in jobs}
    return gantt, miss

if __name__ == "__main__":
    jobs = [
        RTJob("J1", 0, 4, 7),
        RTJob("J2", 2, 2, 4),
        RTJob("J3", 4, 1, 5),
        RTJob("J4", 5, 3, 9),
    ]
    policy = "LLF"
    g, miss = simulate_rt(jobs, policy=policy)
    arrivals={j.name:j.arrive for j in jobs}; total=sum(j.exec for j in jobs)
    m, per = metrics_gantt(g, arrivals, total)
    print("Analysis:", m, per)
    plot_gantt(g, f"Real-Time Scheduling: {policy}")
    print("Deadline Misses:", miss)