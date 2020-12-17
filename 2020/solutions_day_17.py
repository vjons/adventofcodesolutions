import aoc_lib as al
import numpy as np
from scipy.ndimage import convolve


def update(x,D):
    nb=convolve(x,np.ones((3,)*D),int,mode="constant")
    x[:]=x&(nb==4) | (nb==3)


def answers(raw):
    init=np.array([list(r) for r in raw.split("\n")])=="#"
    ISH,ID,N=init.shape,init.ndim,6

    for D in (3,4):
        active=np.zeros([2*N+n for n in ISH]+[2*N+1]*(D-ID),dtype=bool)
        active[tuple([slice(N,N+n) for n in ISH]+[N]*(D-ID))]=init[:]
        [update(active,D) for n in range(N)]
        yield np.sum(active)


if __name__=="__main__":
    al.present_answers(17,answers)