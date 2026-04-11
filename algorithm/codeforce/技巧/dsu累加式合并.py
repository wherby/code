# https://codeforces.com/gym/105709/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0411/solution/cf105709e.md
# 这里按照特征合并，是操作累加式合并。所以可以用DSU解决


import init_setting
from cflibs import *
from lib.UnionFind import *
def main(): 
    n, k, q = MII()
    strs = [[ord(c) - ord('a') for c in I()] for _ in range(n)]
    
    vis = [0] * k
    cur = 1
    
    uf = UnionFind(n)
    outs = []
    
    for _ in range(q):
        query = LII()
        
        if query[0] == 1:
            idx = query[1] - 1
            
            if not vis[idx]:
                vis[idx] = 1
                tmp = [-1] * 10
                
                for i in range(n):
                    if tmp[strs[i][idx]] != -1:
                        uf.merge(tmp[strs[i][idx]], i)
                    tmp[strs[i][idx]] = i
                    cur = fmax(cur, uf.getSize(i))
            
        elif query[0] == 2:
            outs.append(uf.getSize(query[1] - 1))
        else:
            outs.append(cur)
    
    print('\n'.join(map(str, outs)))