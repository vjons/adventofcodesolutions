import aoc_lib as al
import numpy as np


def valid(value,a,b,c,d):
    return ((a<=value) & (value<=b)) | ((c<=value) & (value<=d))


def answers(raw):
#     raw="""class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12"""
    global valid_nbts,result,keys,a,inds
    info,your_ticket,nearby_ticket=raw.split("\n\n")
    info=(row.split(": ") for row in info.split("\n"))
    info={k:[int(x) for x in v.replace(" or ","-").split("-")] for k,v in info}
    your_ticket=np.array([int(x) for x in your_ticket.split("\n")[1].split(",")])
    nbt=np.array([[int(x) for x in row.split(",")] for row in nearby_ticket.split("\n")[1:]])


    yield sum([n for n in nbt.flatten() if all(~valid(n,*args) for args in info.values())])

    valid_nbts=np.array([n for n in nbt if not all(np.any(~valid(n,*args)) for args in info.values())])

    keys=list(info.keys())
    result=[(key,np.all(valid(valid_nbts,*abcd),axis=0).astype(int)) for key,abcd in info.items()]

    result.sort(key=lambda x:np.sum(x[1]))

    done=set()
    indices=[]
    while result:
        k,r=result.pop(0)
        inds=set(np.argwhere(r)[:,0])
        inds=inds-done
        done=set.union(inds,done)
        if k.startswith("departure"):
            indices.append(inds.pop())

    yield np.prod(your_ticket[indices],dtype=np.uint64)

if __name__=="__main__":
    al.present_answers(16,answers)

