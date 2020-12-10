import aoc_lib as al
import numpy as np
import itertools as itr

def answers(raw):
    data=np.sort(np.array(raw.split("\n"),dtype=np.uint64))
    diff=np.r_[1,np.diff(data),3]
    a1=np.sum(diff==1)*np.sum(diff==3)
    a2=np.prod([[1,1,2,4,7][len(s)] for s in "".join(diff.astype(str)).split("3")])
    return a1,a2

al.present_answers(10,answers)