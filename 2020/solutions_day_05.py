import aoc_lib as al
import numpy as np
import re

def answers(raw):
    data=re.sub("F|L","0",re.sub("B|R","1",raw)).split("\n")

    IDS=np.array([int(d,2) for d in data]).T

    missing_IDS=np.array(list(set(range(7,127*8))-set(IDS)))
    
    filt=np.diff(missing_IDS)>1
    your_ID=missing_IDS[:-1][filt][1]

    return np.max(IDS),your_ID

al.present_answers(5,answers)
