import aoc_lib as al
import numpy as np
import itertools as itr
import time

def answers(raw):
    global timestamp,data
    timestamp,data=raw.split("\n")
    data=[(r,int(d)) for r,d in enumerate(data.split(",")) if d!="x"]
    delays=[d-int(timestamp)%d for _,d in data]
    index=np.argmin(delays)
    yield delays[index]*data[index][1]

    a,f=0,1
    for r,d in data:
        a=next(a+n*f for n in itr.count() if (a+n*f+r)%d==0)
        f*=d
    yield a

al.present_answers(13,answers)