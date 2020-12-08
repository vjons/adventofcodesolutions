import aoc_lib as al

def parse(row):
    key,info=row.split(" bags contain ")
    values=info.strip(".").split(",")
    bags=[]
    while values:
        n,v=values.pop(0).strip().split(" ",1)
        if n=="no":
            break
        v=v[:-4].strip()
        bags.append((int(n),v))
    return key,tuple(bags)

def answers(raw):
    data=dict(map(parse,raw.split("\n")))
    val=set(["shiny gold"])
    inval=set()
    checked_keys=set()

    def check(k):
        valid=k not in inval and k in val or any(check(v) for _,v in data[k])
        [inval,val][valid].add(k)
        return valid

    key=iter(data)
    while len(inval)+len(val)<len(data):
        check(next(key))

    count_bags = lambda k: sum(ni+ni*count_bags(ki) for ni,ki in data[k])

    return len(val)-1,count_bags("shiny gold")

al.present_answers(7,answers)