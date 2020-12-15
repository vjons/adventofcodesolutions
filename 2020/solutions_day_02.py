import aoc_lib as al


def validator1(entry):
    r,l,p=entry
    lb,ub=map(int,r.split("-"))
    return lb<=p.count(l[0])<=ub

def validator2(entry):
    r,l,p=entry
    i1,i2=r.split("-")
    return (p[int(i1)-1]==l[0])^(p[int(i2)-1]==l[0])

def answers(raw):
    data=[part.split(" ") for part in raw.split("\n")]
    yield from (len(list(filter(v,data))) for v in (validator1,validator2))

if __name__=="__main__":
    al.present_answers(2,answers)