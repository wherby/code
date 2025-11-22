# https://codeforces.com/gym/106191/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1117/solution/cf106191e.md
#  全集查询就是全图的所有的出度(边的数量)，去掉一个点的补集就是这个点的出度加入度
#  有向图中 边的数量*2 == 所有点出度+ 入度 
#  此题需要查询一个点的出度和入度和为1 为叶子


import init_setting
from cflibs import *
def main(): 
    def query(S, T):
        print('?', len(S), *(i + 1 for i in S), len(T), *(i + 1 for i in T), flush=True)
        return II()
    
    def answer(x):
        print('!', x, flush=True)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        
        total_edge = query(list(range(n)), list(range(n)))
        degs = [0] * n
        
        for i in range(n - 1):
            tmp = [j for j in range(n) if j != i]
            degs[i] = total_edge - query(tmp, tmp)
        
        degs[-1] = total_edge * 2 - sum(degs)
        
        if 1 in degs: answer(degs.index(1) + 1)
        else: answer(-1)