import aoc_lib as al
import numpy as np
from scipy.ndimage import convolve

def answers(raw):
    init=np.array([list(r) for r in raw.split("\n")])=="#"
    niter=6
    dims=(2,3,4,5)
    for D in dims:
        state=np.pad(init[(np.newaxis,)*(D-init.ndim)],niter)
        kernel=np.ones((3,)*D)
        for _ in range(niter):
            neighbors=convolve(state,kernel,int,mode="constant")
            state[:]=state&(neighbors==4) | (neighbors==3)
        yield state.sum()

if __name__=="__main__":
    al.present_answers(2020,17,answers)
