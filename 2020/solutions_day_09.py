import aoc_lib as al
import numpy as np
import itertools as itr

def answer2(s,data):
    for i in itr.count():
        for n in itr.count(start=2):
            test_sum=np.sum(data[i:i+n])
            if test_sum>s:
                break
            elif test_sum==s:
                return np.min(data[i:i+n])+np.max(data[i:i+n])

def answers(raw):
    data=np.array(raw.split("\n")).astype("int64")
    for i,x in enumerate(data[25:]):
        if x not in set(a+b for a,b in itr.combinations(data[i:i+25],2)):
            break
    return x,answer2(x,data)

al.present_answers(9,answers)