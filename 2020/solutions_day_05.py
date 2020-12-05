import aoc_lib as al
import numpy as np
import re

raw=al.get_aoc_input(al.session_cookie,day=5).strip("\n")
data=re.sub("F|L","0",re.sub("B|R","1",raw)).split("\n")

IDS=np.array([int(d,2) for d in data]).T

missing_IDS=np.array(list(set(range(7,127*8))-set(IDS)))

filt=np.diff(missing_IDS)>1
your_ID=missing_IDS[:-1][filt][1]

answer1=np.max(IDS)
answer2=your_ID

print("answer 1:",answer1,"answer 2:",answer2)
