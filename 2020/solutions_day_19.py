import aoc_lib as al
import numpy as np
import re

def answers(raw):
    rules1,messages=raw.split("\n\n")
    rules1=dict([row.replace('"','').split(": ") for row in rules1.split("\n")])
    messages=messages.split("\n")

    rules2=rules1.copy()
    rules2["8"]="42 | 42 8"
    rules2["11"]="42 31 | 42 11 31"

    p=re.compile("\\d+")

    for rs in (rules1,rules2):
        res=0
        while True:
            for k,v in rs.items():
                repls=[f"({rs[m[0]]})" if "|" in rs[m[0]] else rs[m[0]]
                       for m in p.finditer(v)]
                if not repls: continue
                while p.search(rs[k]) is not None:
                    rs[k]=p.sub("{}",rs[k])
                rs[k]=rs[k].format(*repls)
            pattern="^"+rs["0"].replace(" ","")+"$"
            res,old_res=sum(1 for m in messages if re.match(pattern,m)),res
            if res>0 and res==old_res:
                break
        yield res

if __name__=="__main__":
    al.present_answers(2020,19,answers)
