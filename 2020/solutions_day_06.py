import aoc_lib as al

def answers(raw):
        data=[[set(l) for l in group.split("\n")] for group in raw.split("\n\n")]
        return [sum([len(f(*sets)) for sets in data]) for f in (set.union,set.intersection)]

al.present_answers(6,answers)