import aoc_lib as al
import operator as op

id_=lambda x,y:x or y

def evaluate(it,ops,acc=None,op=id_):
    while (not acc or ch not in ops or pr>=-1 and pr!=1) and (ch:=next(it,"")):
        op,pr=ops.get(ch.strip("("),(op,0))
        if pr<=0: acc=op(acc,evaluate(it,ops) if ch in ops else int(ch))
    return acc


def answers(raw):
    data=[r.replace(" ","") for r in raw.split("\n")]
    opers= [{c:(f,p) for c,f,p in zip("+*)(",(op.add,op.mul,None,None),pr+(1,-1))}\
               for pr in [(2,2),(2,-2),(-2,2),(-2,-2)]]
    yield from (sum(evaluate(iter(d),ops) for d in data) for ops in opers)

if __name__=="__main__":
    al.present_answers(2020,18,answers)
