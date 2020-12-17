import aoc_lib as al
import numpy as np
from scipy.ndimage import convolve


def answers(raw):
    init=np.array([list(r) for r in raw.split("\n")])=="#"
    N=6

    for D in (2,3,4,5,6):
        active=np.pad(init[(np.newaxis,)*(D-init.ndim)],N)
        kernel=np.ones((3,)*D)
        for _ in range(N):
            neighbors=convolve(active,kernel,int,mode="constant")
            active[:]=active&(neighbors==4) | (neighbors==3)
        yield np.sum(active)


if __name__=="__main__":
    al.present_answers(17,answers)
