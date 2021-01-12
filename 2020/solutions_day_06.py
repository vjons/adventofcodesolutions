import aoc_lib as al

def answers(raw):
    data=[[set(l) for l in group.split("\n")] for group in raw.split("\n\n")]
    functions=set.union,set.intersection
    yield from (sum([len(f(*sets)) for sets in data]) for f in functions)

if __name__=="__main__":
    al.present_answers(2020,6,answers)