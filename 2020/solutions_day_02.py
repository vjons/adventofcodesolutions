import aoc_lib as al
import numpy as np

raw = al.get_aoc_input(al.session_cookie,day=2).strip("\n")

data=[part.split(" ") for part in raw.split("\n")]

def validator1(entry):
    r,l,p=entry
    lb,ub=map(int,r.split("-"))
    return lb<=p.count(l[0])<=ub

def validator2(entry):
    r,l,p=entry
    i1,i2=map(int,r.split("-"))
    return (p[i1-1]==l[0])+(p[i2-1]==l[0])==1

answer1=len(list(filter(validator1,data)))
answer2=len(list(filter(validator2,data)))


print("answer 1:",answer1,"answer 2:",answer2)