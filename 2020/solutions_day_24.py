import aoc_lib as al
import numpy as np
from scipy.ndimage import convolve
from collections import Counter

T=dict(nw=(-1,-1),ne=(-1,0),w=(0,-1),e=(0,1),sw=(1,0),se=(1,1))
kernel=1-np.eye(3)[::-1]

def parse(path):
    while path: yield np.array(T.get(d:=path.pop(0)) or T.get(d+path.pop(0)))

def answers(raw):
    data=Counter([tuple(sum(parse(list(r)))) for r in raw.split("\n")])
    coords=np.array([k for k,v in data.items() if v%2]).T
    yield len(coords[0])
    init=np.zeros(np.ptp(coords,axis=1)+1,dtype=int)
    init[tuple(coords-np.min(coords,axis=1,keepdims=True))]=1
    black_tiles=np.pad(init,100)
    for _ in range(100):
        nbs=convolve(black_tiles,kernel,mode="constant")
        black_tiles[:]=black_tiles&(nbs==1) | (nbs==2)
    yield np.sum(black_tiles)

if __name__=="__main__":
    al.present_answers(2020,24,answers)