import aoc_lib as al
import numpy as np
import itertools as itr
from operator import add,mul

ops={"*":mul,"+":add,"R":mul,"L":mul}
ids={"*":1,"+":0}

print(592002768446)

#local and global accumulator

#if prec==+*
#local=0, global=1
#when op is None:
    #local=value
#when op is +
    #local+=value
#when op is *
    #global*=local
    #local=0
#when done
    #return global

#if prec=="*+":
#local=1, global=0
#when op is None:
    #local=value
#when op is *
    #local*=value
#when op is +
    #global+=local
    #local=1
#when done
    #return global

#if prec=="LR":
#local=1,global=0
#when op is None:
    #global=value
#when op is *
    #global*=value
#when op is +
    #global+=value
#when done
    #return global

#if prec=="RL":
#local=1,global=0
#when op is None:
    #global=value
#when op is *
    #return global*evaluate(rest,prec,acc,op)
#when op is +
    #return global+evaluate(rest,prec,acc,op)
#when done
    #return ops[op]

def evaluate(data,prec,op="+",term=0,factor=None):
    if factor is None:
        factor = 0 if prec=="*+" else 1
    try:
        char=next(data)
    except:
        return factor+term if prec=="*+" else factor*term
    if char in "+*":
        op=char
    elif char not in (" )"):
        if char=="(":
            pc=[1]
            f=lambda x: (pc.append(pcs.get(x,0)),sum(pc))[1]
            value=evaluate((d for d in itr.takewhile(f,data)),prec)
        else:
            value=int(char)
        if prec=="L2R":
            term=eval(f"term{op}value")
        elif prec=="+*":
            if op=="+":
                term+=value
            else:
                factor*=term
                term=value
        elif prec=="*+":
            if op=="*":
                factor*=value
            else:
                term+=factor
                factor=value

                
                
    return evaluate(data,prec,op,term,factor)


    # elif char==")":
    #     return None
    # elif char=="(":
    #     value=evaluate(data,prec)
    # else:
    #     value=int(char)
    #     op=next(data)

    # if acc is None:
    #     acc==value

    # if prec=="LR":
    #     acc=ops[op](acc,value)
    # # elif prec=="RL":
    # #     return ops[op](value,evaluate(data,prec))
    # # else:
    # #     if op==prec[0]:
    # #         acc=ops[op](acc,value)
    # #     else:
    # #         return ops[op](acc,evaluate(data,prec))
    # result=evaluate(data,prec,acc)
    # return acc if result is None else result

# def evaluate(data,prec,acc=None,op=None):
#     char=next(data,")")
#     # print("N" if acc is None else acc,"N" if op is None else op,char)
#     if char==")":
#         return None
#     elif char in ops:
#         return evaluate(data,prec,acc,char)
#     elif char=="(":
#         value=evaluate(data,prec)
#     else:
#         value=int(char)
#     if acc==None:
#         return evaluate(data,prec,value,char)
#     if prec=="LR":
#         acc=ops[op](acc,value)
#         ret=evaluate(data,prec,acc,op)
#         return acc if ret is None else ret
#     elif prec=="RL":
#         ret=evaluate(data,prec,value)
#         if ret is None:
#             return acc
#         return ops[op](acc,ret)
    #     return value if ret is None else ops[op](value,ret)
    # if prec=="RL":
    #     return ops[op](value,evaluate(data,prec))
    # elif prec=="+*":
    #     if op==prec[0]:
    #         acc=ops[op](acc,value)
    #         return evaluate(data,prec,acc)
    #     else:
    #         print("")
    #         # ret=
    #         return ops[op](acc,evaluate(data,prec,value))
            # acc=value

    # return acc if ret is None else ret


def answers(raw):
    # raw="""(2+4)*2+4*3"""
    data=[r.replace(" ","") for r in raw.split("\n")]
    yield from (sum([evaluate(iter(d),prec) for d in data]) for prec in ("LR","+*","*+"))



if __name__=="__main__":
    al.present_answers(18,answers)
