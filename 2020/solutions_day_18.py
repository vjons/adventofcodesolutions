import aoc_lib as al
import numpy as np
import itertools as itr
from operator import add,mul

ops={"*":mul,"+":add,"R":mul,"L":mul}
ids={"*":1,"+":0}

#Did it first then tried to clean up the code and broke it
#Will fix it later
def evaluate(data,prec):
    pass
    # ,op="+",term=0,factor=None):
#     if factor is None:
#         factor = 0 if prec=="*+" else 1
#     try:
#         char=next(data)
#     except:
#         return factor+term if prec=="*+" else factor*term
#     if char in "+*":
#         op=char
#     elif char not in (" )"):
#         if char=="(":
#             pc=[1]
#             f=lambda x: (pc.append(pcs.get(x,0)),sum(pc))[1]
#             value=evaluate((d for d in itr.takewhile(f,data)),prec)
#         else:
#             value=int(char)
#         if prec=="L2R":
#             term=eval(f"term{op}value")
#         elif prec=="+*":
#             if op=="+":
#                 term+=value
#             else:
#                 factor*=term
#                 term=value
#         elif prec=="*+":
#             if op=="*":
#                 factor*=value
#             else:
#                 term+=factor
#                 factor=value

#     return evaluate(data,prec,op,term,factor)

def answers(raw):
    data=[r.replace(" ","") for r in raw.split("\n")]
    yield from (sum(evaluate(iter(d),prec) for d in data) for prec in ("LR","+*"))

if __name__=="__main__":
    al.present_answers(2020,18,answers)
