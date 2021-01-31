import aoc_lib as al
import operator as op

id_=lambda x,y:y

def evaluate(it,ops,pr0=0,acc=None,op_pr=(id_,0)):
    while ((not acc) or ch not in ops or pr0<op_pr[1]) and (ch:=next(it,")"))!=")":
        if (op_pr:=ops.get(ch,(op_pr[0],pr0)))[1]<=pr0:
            acc = op_pr[0](acc,evaluate(it,ops,op_pr[1]) if ch in "(+*"  else int(ch))
    return acc

def answers(raw):
    data=[r.replace(" ","") for r in raw.split("\n")]
    opss= [{c:(f,p) for c,f,p in zip("+*)",(op.add,op.mul,id_,id_),pr+(10,))}\
               for pr in [(2,2),(2,-2),(-2,2),(-2,-2)]]
    yield from (sum(evaluate(iter(d),ops) for d in data) for ops in opss)

if __name__=="__main__":
    al.present_answers(2020,18,answers)
