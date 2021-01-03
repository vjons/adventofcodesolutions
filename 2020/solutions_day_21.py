import aoc_lib as al

def parse(r):
    f,a=r.split(" (contains ")
    a=a.replace(" ","").strip(")").split(",")
    return set(f.split()),set(a)

def answers(raw):
    foods,alles=zip(*(parse(r) for r in raw.split("\n")))
    all_ings=set.union(*foods)
    all_alls=set.union(*alles)
    uniques={key:set.intersection(*(f for f,a in zip(foods,alles) if key in a))\
             for key in all_alls}

    ing_dict=[]
    while uniques:
        kr,rv=next((k,v) for k,v in uniques.items() if len(v)==1)
        ing_dict.append((kr,list(uniques.pop(kr))[0]))
        for v in uniques.values(): v-=rv

    _,free_ings=zip(*sorted(ing_dict))
    dang_ings=all_ings-set(free_ings)

    yield sum(sum(1 for ing in food if ing in dang_ings) for food in foods)
    yield ",".join(free_ings)

if __name__=="__main__":
    al.present_answers(2020,21,answers)