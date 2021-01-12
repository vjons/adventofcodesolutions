import aoc_lib as al
import numpy as np

def answers(raw):
    init=[int(n) for n in raw.split(",")]
    L=len(init)
    for N in (2020,30000000):
        ns=np.zeros(N,dtype=int)
        ns[init[:-1]]=range(1,L)
        ln=init[-1]
        for i in range(L,N):
            n, ns[ln] = ns[ln], i
            ln = i - n if n else 0
        yield ln

if __name__=="__main__":
    al.present_answers(2020,15,answers)