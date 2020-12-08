import aoc_lib as al
from time import time
import numpy as np
import itertools as itr
import functools as fts
from memory_profiler import memory_usage

def answers(raw):
    data = np.array(raw.split("\n")).astype(int)
    
    a=np.add.outer
    m=np.multiply.outer

    ext_sum1=fts.reduce(a,[data]*2)
    ext_prod1=fts.reduce(m,[data]*2)

    answer1=ext_prod1[ext_sum1==2020][0]

    ext_sum=fts.reduce(a,[data]*3)
    ext_prod=fts.reduce(m,[data]*3)

    answer2=ext_prod[ext_sum==2020][0]

    return answer1,answer2

if __name__ == '__main__':

    raw = al.get_aoc_input(al.session_cookie,day=1).strip("\n")

    a1,a2=answers(raw)
    t0=time()
    for _ in range(100):
        answers(raw)

    print("Answer 1:",a1)
    print("Answer 2:",a2)
    print(f"Running time: {(time()-t0)/100:.4f}")
    print("Max RAM used:",max(memory_usage((answers,(raw,),{}))))

