import aoc_lib as al
from time import time
import numpy as np
import itertools as itr
import functools as fts

def answers(raw):
    data = np.array(raw.split("\n")).astype(int)
    
    a=np.add.outer
    m=np.multiply.outer

    ext_sum1=fts.reduce(a,[data]*2)
    ext_prod1=fts.reduce(m,[data]*2)

    answer1=ext_prod1[ext_sum1==2020][0]

    ext_sum2=fts.reduce(a,[data]*3)
    ext_prod2=fts.reduce(m,[data]*3)

    answer2=ext_prod2[ext_sum2==2020][0]

    return answer1,answer2


if __name__=="__main__":
    al.present_answers(1,answers,100)

