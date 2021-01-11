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

def labels(after,start,count):
    if count:
        yield after[start]+1
        yield from labels(after,after[start],count-1)

def answers(raw):
    init=np.array([int(r)-1 for r in raw])
    after=play(init,100)
    yield "".join(map(str,labels(after,0,8)))
    after=play(np.r_[init,np.mgrid[len(init):10**6]],10**7)
    yield np.prod(list(labels(after,0,2)),dtype=np.int64)

if __name__=="__main__":
    al.present_answers(2020,23,answers)