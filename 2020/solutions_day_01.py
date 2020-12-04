import aoc_lib as al
import numpy as np

raw = al.get_aoc_input(al.session_cookie,day=1).strip("\n")
data = np.array(raw.split("\n")).astype(int)

ext_sum1=data[None,:]+data[:,None]
ext_prod1=data[None,:]*data[:,None]

answer1=ext_prod1[ext_sum1==2020][0]

ext_sum2=data[None,None,:]+data[None,:,None]+data[:,None,None]
ext_prod2=data[None,None,:]*data[None,:,None]*data[:,None,None]

answer2=ext_prod2[ext_sum2==2020][0]

print("answer 1:",answer1,"answer 2:",answer2)
