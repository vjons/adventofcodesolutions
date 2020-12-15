import aoc_lib as al

cmds=dict(N=(1j,1),S=(-1j,1),E=(1,1),W=(-1,1),L=(0,1j),R=(0,-1j))


def answers(raw):
    instructions=[(r[0],int(r[1:])) for r in raw.split("\n")]
    for part2,d in enumerate((1,10+1j)): 
        z=0j
        for inst,val in instructions:
            if inst=="F":
                z+=d*val
                continue
            c,m=cmds[inst]
            d*=m**(val/90)
            if part2:
                d+=c*val
            else:
                z+=c*val
        yield int(abs(z.real)+abs(z.imag))


if __name__=="__main__":
    al.present_answers(12,answers)