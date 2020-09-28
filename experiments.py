from experiments.experiment_one import *


results = {}
for i in range(100):
    w = minimax_vs_memcts(iters=150,fname=f'iters_150_{i}')
    results[w] = results.get(w, 0) + 1
with open("experimentos.csv","a") as f:
    f.write(f"minimax,memcts_150,{results.get(0,0)},{results.get(1,0)},{results.get(2,0)}")


def mmexp(i1,i2):
    print(f"Started experiment:{i1},{i2}")
    results = {}
    for i in range(100):
        w = memcts_vs_memcts(iters1=i1,iters2=i2,fname=f'iters_{i1}vs{i2}_{i}')
        results[w] = results.get(w, 0) + 1
    with open("experimentos.csv","a") as f:
        f.write(f"memcts_{i1},memcts_{i2},{results.get(0,0)},{results.get(1,0)},{results.get(2,0)}\n")

mmexp(150,150)
mmexp(150,500)
mmexp(500,500)
mmexp(500,1000)
mmexp(1000,500)
mmexp(1000,2000)
mmexp(2000,1000)
mmexp(2000,3000)
mmexp(3000,2000)


print(results)