import aoc_lib as al

N=20201227

def answers(raw):
    pk1,pk2=map(int,raw.split("\n"))
    loop_size=next(p for p in range(N) if pow(7,p,N)==pk1)
    yield pow(pk2,loop_size,N)

if __name__=="__main__":
    al.present_answers(2020,25,answers)