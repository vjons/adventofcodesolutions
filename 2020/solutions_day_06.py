import aoc_lib as al

raw=al.get_aoc_input(al.session_cookie,day=6).strip("\n")

data=[[set(l) for l in group.split("\n")] for group in raw.split("\n\n")]

answer1=sum([len(set.union(*sets)) for sets in data])
answer2=sum([len(set.intersection(*sets)) for sets in data])

print("answer 1:",answer1,"answer 2:",answer2)