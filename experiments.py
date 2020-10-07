from experiments.experiment_one import *


#results = {}
#for i in range(100):
#    w = minimax_vs_memcts(iters=450,fname=f'iters_450_{i}')
#        results[w] = results.get(w, 0) + 1
#with open("experimentos.csv","a") as f:
#    f.write(f"memcts_450,minimax,{results.get(0,0)},{results.get(1,0)},{results.get(2,0)}\n")


def mmexp(i1,i2,c1="best_child",fn1=None,c2="best_child",fn2=None):
    print(f"Started experiment:{i1},{i2}")
    results = {}
    for i in range(15):
        w = memcts_vs_memcts(iters1=i1,iters2=i2,fname=f'iters_{i1}vs{i2}_{i}',c1=c1,fn1=fn1,c2=c2,fn2=fn2)
        results[w] = results.get(w, 0) + 1
    with open("experimentos.csv","a") as f:
        f.write(f"memcts_{i1},memcts_{i2},{results.get(0,0)},{results.get(1,0)},{results.get(2,0)}\n")



#mmexp(150,150)
#mmexp(150,500)
#mmexp(500,500)
#mmexp(500,1000)
#mmexp(1000,500)
#mmexp(1000,2000)
#mmexp(2000,1000)
#mmexp(2000,3000)
mmexp(300,300,c1="",fn1=lambda x:x.q,c2="",fn2=lambda x:x.n)
mmexp(301,301,c1="",fn1=lambda x:x.n,c2="",fn2=lambda x:x.q)

mmexp(302,302,c1="",fn1=lambda x:x.q)
mmexp(303,303,c2="",fn2=lambda x:x.q)

mmexp(299,299,c1="",fn1=lambda x:x.n)
mmexp(298,298,c2="",fn2=lambda x:x.n)
