import aoc_lib as al
import numpy as np
import itertools as itr

def answers(raw):
    data=np.array(raw.split("\n")).astype("int64")

    for i,ref_sum in enumerate(data[25:]):
        if ref_sum not in set(a+b for a,b in itr.combinations(data[i:i+25],2)):
            yield ref_sum
            break

    for i in itr.count():
        for n in itr.count(start=2):
            test_sum=np.sum(data[i:i+n])
            if test_sum>ref_sum:
                break
            if test_sum==ref_sum:
                yield np.min(data[i:i+n])+np.max(data[i:i+n])
                break

if __name__=="__main__":
    al.present_answers(2020,9,answers)