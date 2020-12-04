import aoc_lib as al
import numpy as np

raw = al.get_aoc_input(al.session_cookie,day=3).strip("\n")
data=raw.replace(".","0 ").replace("#","1 ")

forrest=np.array([line.strip().split(" ") for line in data.split("\n")]).astype("int64")
forrest=np.tile(forrest,(1,100))

path=np.array([np.sum(np.diag(forrest[::n,::m])) for n,m in zip((1,1,1,1,2),(1,3,5,7,1))])

print("answer 1:", path[1],"answer 2:", np.prod(path))
