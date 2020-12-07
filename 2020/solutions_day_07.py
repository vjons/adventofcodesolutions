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
        bags.append([int(n),v])
    return key,bags


data=dict(map(parse,raw))

def validate(k,keys=[]):
    new_keys=keys+[k]
    if keys and k=="shiny gold":
        return True
    elif len(new_keys)>1 and new_keys[0]==new_keys[-1]:
        return False
    else:
        return any(validate(v,new_keys) for n,v in data[k])


def count_bags(k):
    return sum(ni+ni*count_bags(ki) for ni,ki in data[k])

answer1=len(list(filter(validate,data.keys())))
answer2=count_bags("shiny gold")

print("answer 1:",answer1,"answer 2:",answer2)