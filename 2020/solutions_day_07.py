import aoc_lib as al

raw=al.get_aoc_input(al.session_cookie,day=7).strip("\n").split("\n")

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

data=dict(map(parse,raw))
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

answer1=len(val)-1
answer2=count_bags("shiny gold")

print("answer 1:",answer1,"answer 2:",answer2)