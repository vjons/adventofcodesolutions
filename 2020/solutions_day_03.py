import aoc_lib as al
import numpy as np


def answers(raw):
    data=raw.replace(".","0 ").replace("#","1 ")

    forrest=np.array([line.strip().split(" ") for line in data.split("\n")]).astype("int64")
    forrest=np.tile(forrest,(1,100))

    path=np.array([np.sum(np.diag(forrest[::n,::m])) for n,m in zip((1,1,1,1,2),(1,3,5,7,1))])

    return path[1],np.prod(path)

if __name__=="__main__":
    al.present_answers(3,answers)
