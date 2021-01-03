import aoc_lib as al

def parse(r):
    f,a=r[:-1].split(" (contains")
    a=a.replace(" ","").split(",")
    return set(f.split()),set(a)

def answers(raw):
    fa=list(zip(*(parse(r) for r in raw.split("\n"))))
    all_ings,all_alls=(set.union(*x) for x in fa)
    uniques={key:set.intersection(*(f for f,a in zip(*fa) if key in a))\
             for key in all_alls}

    free_ai=[]
    while uniques:
        kr,rv=next((k,v) for k,v in uniques.items() if len(v)==1)
        free_ai.append((kr,list(uniques.pop(kr))[0]))
        for v in uniques.values(): v-=rv

    _,free_ings=zip(*sorted(free_ai))
    dang_ings=all_ings-set(free_ings)

    yield sum(sum(1 for ing in food if ing in dang_ings) for food in fa[0])
    yield ",".join(free_ings)

if __name__=="__main__":
    al.present_answers(2020,21,answers)