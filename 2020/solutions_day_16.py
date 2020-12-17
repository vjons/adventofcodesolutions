import aoc_lib as al
import numpy as np


def valid(value,a,b,c,d):
    return ((a<=value) & (value<=b)) | ((c<=value) & (value<=d))


def answers(raw):
    info,your_ticket,nearby_ticket=raw.split("\n\n")
    info=(row.split(": ") for row in info.split("\n"))
    info={k:[int(x) for x in v.replace(" or ","-").split("-")] for k,v in info}
    your_ticket=np.array([int(x) for x in your_ticket.split("\n")[1].split(",")])
    nbt=np.array([[int(x) for x in row.split(",")] for row in nearby_ticket.split("\n")[1:]])

    #Part 1
    yield sum([n for n in nbt.flatten() if all(~valid(n,*args) for args in info.values())])

    #Part 2
    valid_nbts=np.array([n for n in nbt if not all(np.any(~valid(n,*args)) for args in info.values())])
    pairs=[(key,np.all(valid(valid_nbts,*abcd),axis=0).astype(int)) for key,abcd in info.items()]
    pairs.sort(key=lambda x:np.sum(x[1]))
    keys,locations=zip(*pairs)
    indices=np.argsort(-np.sum(locations,axis=0))
    indices=[ind for key,ind in zip(keys,indices) if key.startswith("departure")]
    yield np.prod(your_ticket[indices],dtype=np.uint64)

if __name__=="__main__":
    al.present_answers(16,answers)

