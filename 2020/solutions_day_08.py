import aoc_lib as al

process=lambda cmd,arg,p,v:{"jmp":(p+arg,v),"acc":(p+1,v+arg),"nop":(p+1,v)}[cmd]

def run(code):
    positions=set([0])
    pos=0
    value=0
    while pos<len(code):
        pos,value=process(*code[pos],pos,value)
        if pos in positions:
            return False,value
        positions.add(pos)
    return True,value

def answers(raw):
    program=[[cmd[:3],int(cmd[4:])] for cmd in raw.split("\n")]
    for i,d in enumerate(program):
        d_mem=d[0]
        if d=="acc":
            continue
        d[0]=("nop","jmp")[d=="nop"]
        terminated,value=run(program)
        d[0]=d_mem
        if terminated:
            break
    return run(program)[1],value

al.present_answers(8,answers)