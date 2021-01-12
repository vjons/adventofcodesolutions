import aoc_lib as al
import numpy as np

def to_array(value,length):
    return np.array(list(f"{value:0>{length}b}"))

def to_int(value):
    return int("".join(value),2)

def answers(raw):
    mem1={}
    mem2={}
    for row in raw.split("\n"):
        if row.startswith("mask"):
            mask=np.array(list(row[7:]))
            at_X=mask=="X"
            at_1=mask=="1"
            L=np.sum(at_X)
            continue
        adress,value=map(int,row[4:].split("] = "))

        bin_value=to_array(value,36)
        bin_value[~at_X]=mask[~at_X]
        mem1[adress]=to_int(bin_value)

        bin_adress=to_array(adress,36)
        bin_adress[at_1]="1"
        for x in range(2**L):
            bin_adress[at_X]=to_array(x,L)
            mem2[to_int(bin_adress)]=value

    yield from (sum(m.values()) for m in (mem1,mem2))

if __name__=="__main__":
    al.present_answers(2020,14,answers)