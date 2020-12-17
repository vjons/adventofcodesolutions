import aoc_lib as al
import numpy as np
from scipy.ndimage import convolve

def update1(st):
    nbs=convolve(st,np.ones((3,3,3)),int,mode="constant",cval=0)
    return (st&((nbs==3)|(nbs==4))) | (~st&(nbs==3)),st.copy()


def update2(st):
    nbs=convolve(st,np.ones((3,3,3,3)),int,mode="constant",cval=0)
    return (st&((nbs==3)|(nbs==4))) | (~st&(nbs==3)),st.copy()


def answers(raw):
    init=np.array([list(r) for r in raw.split("\n")])=="#"
    n1,n2=init.shape
    n=max(n1,n2)+7
    for upd,dim in ((update1,3),(update2,4)):
        shape=(2*n,)*dim
        active=np.zeros(shape,dtype=bool)
        sl=(slice(n,n+n1),slice(n,n+n2))+(n,)*(dim-2)
        active[sl]=init.copy()
        for i in range(6):
            active,ref=upd(active)
        yield np.sum(active)

if __name__=="__main__":
    al.present_answers(17,answers)