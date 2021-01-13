import aoc_lib as al
import operator as op

operators = {"*":op.mul,"+":op.add}
precedences = ("LR","+*","*+","RL")

def evaluate(data,prec):
    operate = None
    while (char:=next(data,")"))!=")":
        if char in operators:
            operate = operators[char]
            if prec[-1] in (char,"L"):
                return operate(acc,evaluate(data,prec))
            continue
        value = evaluate(data,prec) if char == "(" else int(char)
        acc = value if operate is None else operate(acc,value)
    return acc

def answers(raw):
    data=[r.replace(" ","") for r in raw.split("\n")]
    yield from (sum(evaluate(iter(d),p) for d in data) for p in precedences)

if __name__=="__main__":
    al.present_answers(2020,18,answers)
