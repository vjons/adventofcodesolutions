import aoc_lib as al
import numpy as np
import functools as fts


def answers(raw):
    data = np.array(raw.split("\n")).astype(int)
    
    a=np.add.outer
    m=np.multiply.outer

    #Part 1
    ext_sum1=fts.reduce(a,[data]*2)
    ext_prod1=fts.reduce(m,[data]*2)
    yield ext_prod1[ext_sum1==2020][0]

    #Part 2
    ext_sum2=fts.reduce(a,[data]*3)
    ext_prod2=fts.reduce(m,[data]*3)
    yield ext_prod2[ext_sum2==2020][0]


if __name__=="__main__":
    al.present_answers(1,answers)

