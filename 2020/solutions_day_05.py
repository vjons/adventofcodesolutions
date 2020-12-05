import aoc_lib as al
import numpy as np

raw=al.get_aoc_input(al.session_cookie,day=5).strip("\n")
data=raw.replace("B","1").replace("F","0").replace("R","1").replace("L","0").split("\n")

IDS=np.array([int(d[:-3],2)*8+int(d[-3:],2) for d in data]).T

missing_IDS=np.array(list(set(range(7,127*8))-set(IDS)))

filt=np.gradient(missing_IDS)>1
your_ID=missing_IDS[filt][1]

answer1=np.max(IDS)
answer2=your_ID

print("answer 1:",answer1,"answer 2:",answer2)
