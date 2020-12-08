import aoc_lib as al

raw=al.get_aoc_input(al.session_cookie,day=8).strip("\n")

data=[cmd.split(" ") for cmd in raw.split("\n")]

def execute(code):
    global_value=0
    positions=set([0])
    pos=0
    while pos<len(code):
        op,value=code[pos]
        if op=="jmp":
            pos+=int(value)
        elif op=="acc":
            global_value+=int(value)
            pos+=1
        else:
            pos+=1
        if pos in positions:
            break
        else:
            positions.add(pos)
    return pos,global_value

def fix_code():
    for i,(d,v) in enumerate(data):
        changed_code=[d[:] for d in data]
        if d in ("nop","jmp"):
            changed_code[i][0]="jmp" if d=="nop" else "nop"
        else:
            continue
        pos,value=execute(changed_code)
        if pos == len(data):
            return value


answer1=execute(data)[1]
answer2=fix_code()

print("answer 1:",answer1,"answer 2:",answer2)