import aoc_lib as al
import numpy as np

def nways(n,k):
    return 1 if n<2 else 2**(n-1-k)*(2**k-n+k)

def answers(raw):
    data=np.sort(np.array(raw.split("\n"),dtype=np.uint64))
    diff=np.r_[1,np.diff(data),3].astype(np.uint64)

    yield np.sum(diff==1)*np.sum(diff==3)

    nc=[nways(len(s),3) for s in "".join(diff.astype(str)).split("3")]
    yield np.prod(nc,dtype=np.uint64)

if __name__=="__main__":
    al.present_answers(2020,10,answers)