import aoc_lib as al
import numpy as np
import itertools as itr

def nways(n,k):
    if n<2:
        return 1
    return 2**(n-1-k)*(2**k-n+k)

def answers(raw):
    data=np.sort(np.array(raw.split("\n"),dtype=np.uint64))
    diff=np.r_[1,np.diff(data),3].astype(np.uint64)
    a1=np.sum(diff==1)*np.sum(diff==3)
    a2=np.prod([nways(len(s),3) for s in "".join(diff.astype(str)).split("3")],dtype=np.uint64)
    return a1,a2

al.present_answers(10,answers)