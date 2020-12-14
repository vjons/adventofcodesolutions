import aoc_lib as al
import numpy as np
import itertools as itr
from scipy.ndimage import convolve,convolve1d

def update1(st,fl):
    nb=convolve(st,np.ones((3,3)),int,mode="constant",cval=0)
    return (st&(nb<5)) | (nb==0) & ~fl,st.copy()

def update2(st,fl,inds):
    global ps,nbs
    ps=np.pad(st,pad_width=1, mode='constant', constant_values=0)
    nbs=np.zeros(ps.shape)
    for i1,i2 in zip(inds[::2],inds[1::2]):
        nbs[i1,i2]+=convolve1d(ps[i1,i2],(1,0,1))
    nbs=nbs[1:-1,1:-1]
    return (st&(nbs<5)) | (nbs==0) & ~fl,st.copy()


def padded_dir_inds(floor):
    global all_inds
    padded_floor=np.pad(floor,pad_width=1, mode='constant', constant_values=False)
    nr,nc=padded_floor.shape
    inds=np.indices((nr,nc))
    inds[:,padded_floor]=-1
    all_inds=[np.concatenate([np.diag(ind,k) for k in range(1-nr,nc)])\
               for ind in [inds[0],inds[1],inds[0,::-1],inds[1,::-1]]]
    all_inds.extend([inds[0],inds[1],inds[0].T,inds[1].T])
    return [d[d>-1] for d in all_inds]


def display(st,fl=None):
    out=st.astype(str)
    out[out=="-1" if fl is None else fl]="."
    out[out=="1"]="#"
    out[out=="0"]="L"
    print("\n".join(["".join(o) for o in out]))
    print("")


def answers(raw):
    floor=np.array([list(r) for r in raw.split("\n")])=="."
    inds=padded_dir_inds(floor)
    for upd,args in [(update1,(floor,)),(update2,(floor,inds,))]:
        seats=1-floor
        while True:
            seats,ref=upd(seats,*args)
            if np.all(ref==seats):
                yield np.sum(seats)
                break

al.present_answers(11,answers)