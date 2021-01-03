import aoc_lib as al
import numpy as np
from scipy.ndimage import convolve

T = [lambda x:x[:],lambda x:x.T[::-1],lambda x:x[::-1,::-1],lambda x:x[::-1].T,
     lambda x:x[::-1],lambda x:x.T,lambda x:x[:,::-1],lambda x:x[::-1,::-1].T,]

model=np.array([[1,2],[3,4]])
ref = {tuple(tr(model).flat):k for k,tr in enumerate(T)}
Tmul = np.array([[ref[tuple(tb(ta(model)).flat)] for tb in T] for ta in T])
Tinv = np.argwhere(Tmul==0)[:,1]

def parse(photo):
    photo=photo.replace("#","1").replace(".","0")
    header,*pixels=photo.split("\n")
    id_=int(header[5:-1])
    pixels=np.array([list(p) for p in pixels])
    edges=[int("".join(tr(pixels)[0]),2) for tr in T]
    return id_,pixels.astype(int),edges


def populate(ps,links,info):
    i_dest0,trans0,i_src0=info
    for dir_,index_diff in enumerate([-12,1,12,-1]):
        edge_out0=Tmul[trans0,dir_]
        i_src1,edge_match1=links[i_src0,edge_out0]
        i_dest1=i_dest0+index_diff
        if i_src1>-1 and -1<i_dest1<len(ps) and ps[i_dest1][0]==-1:
            trans_fit1=Tmul[edge_match1,Tinv[(edge_out0+4)%8]]
            trans1=Tmul[trans_fit1,trans0]
            ps[i_dest1]=trans1,i_src1
            populate(ps,links,(i_dest1,trans1,i_src1))


def answers(raw):
    ids,pixels,edges=map(np.array,zip(*map(parse,raw.split("\n\n"))))

    ms=np.argwhere(edges[:,:,None,None]==edges)
    ms=ms[ms[:,0]!=ms[:,2]]
    links=np.full((L,8,2),-1)
    links[tuple(ms[:,:2].T)]=ms[:,2:]

    L=len(edges)
    ps=np.full((2*L,2),-1)
    ps[L]=0,0
    populate(ps,links,(L,0,0))
    ps=ps[ps[:,0]!=-1]

    yield np.prod(ids[ps[[0,11,-12,-1],1]],dtype=np.int64)

    tr_pixels=[T[tr](pixels[i_src])[1:-1,1:-1] for tr,i_src in ps]
    full_image=np.moveaxis(np.reshape(tr_pixels,(12,12,8,8)),2,1).reshape(96,96)
    kernel=["                  #  ",
            "#    ##    ##    ### ",
            " #  #  #  #  #  #    "]
    kernel=(np.array([list(row) for row in kernel])=="#").astype(int)
    N=kernel.sum()
    matches=[convolve(full_image,tr(kernel),mode="constant")==N for tr in T]
    
    yield np.sum(full_image)-np.sum(matches)*N


if __name__=="__main__":
    al.present_answers(2020,20,answers)