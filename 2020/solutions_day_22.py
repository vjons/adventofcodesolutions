import aoc_lib as al

def play(d1,d2,rec):
    d1_mem,d2_mem=set(),set()
    while d1 and d2:
        if rec:
            td1,td2=tuple(d1),tuple(d2)
            if td1 in d1_mem and td2 in d2_mem: return 0,d1
            d1_mem.add(td1)
            d2_mem.add(td2)
        c1,c2=d1.pop(0),d2.pop(0)
        w=c2>c1
        if rec and len(d1)>=c1 and len(d2)>=c2:
            w,_=play(d1[:c1],d2[:c2],rec)
        wd=(d1,d2)[w]
        wd.extend((c1,c2)[::1-2*w])
    return w,wd

def answers(raw):
    global winner,deck
    d1,d2=([int(c) for c in r.split("\n")[1:]] for r in raw.split("\n\n"))
    for rec in (0,1):
        _,wd=play(d1.copy(),d2.copy(),rec)
        yield sum(i*c for i,c in enumerate(wd[::-1],start=1))

if __name__=="__main__":
    al.present_answers(2020,22,answers)