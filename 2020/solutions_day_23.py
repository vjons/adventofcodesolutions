import aoc_lib as al
import numpy as np
from numba import njit

@njit
def move(after,current):
    c1=after[current]
    c2=after[c1]
    c3=after[c2]
    dest=current
    while (dest:=dest-1)%len(after) in (c1,c2,c3): pass
    after[current]=after[c3]
    after[c3]=after[dest]
    after[dest]=c1
    return after[current]

@njit
def play(init,move_count):
    after=np.zeros_like(init)
    after[init]=np.roll(init,-1)
    current=init[0]
    for _ in range(move_count):
        current=move(after,current)
    return after

def labels(after,count,start=0):
    if count:
        yield after[start]+1
        yield from labels(after,count-1,after[start])

def answers(raw):
    init1=np.array([int(r)-1 for r in raw])
    yield "".join(map(str,labels(play(init1,100),len(init1)-1)))
    init2=np.r_[init1,np.mgrid[len(init1):10**6]]
    yield np.prod(list(labels(play(init2,10**7),2)),dtype=np.int64)

if __name__=="__main__":
    al.present_answers(2020,23,answers)