# https://codeforces.com/gym/102569/problem/D?__cf_chl_tk=r0CX2fUBM3rQiMjPhzCrbhm5Or.njknVbD7euJqnXKM-1773546253-1.0.1.1-te.NPmjQq47dx6nQGaIj4eEBySL1DeSp_VuAQ8hs.Co
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0314/solution/cf102569d.md
# 双重广度优先搜索 (Two-pass BFS) 寻找一条路， 不仅距离最短也需要字典序最短
# 需要从终点开始 BFS， 记录每个点到终点的距离。 然后从起点开始 BFS， 每次优先选择字典序最小的边， 直到到达终点。
# 如果从起点开始BFS的时候，当前点有可能无法以最短的路径达到终点。 algorithm/codeforce/docs/双重广度优先搜索.md
# 所以用终点开始BFS，记录了距离场，后续从起点开始遍历的时候，就能知道下一个端点是否在最短路径上
# algorithm/codeforce/docs/双重广度优先搜索.md
# 利用记录的距离场，找到下一个点的最小值，然后在满足距离场和下一个最小值的条件下，实现BFS，记录父节点，直到到达终点。 algorithm/codeforce/docs/双重广度优先搜索.md
# 利用父节点恢复路径


import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    us = []
    vs = []
    chs = []
    
    path = [[] for _ in range(n)]
    
    for i in range(m):
        u, v, ch = LI()
        u = int(u) - 1
        v = int(v) - 1
        path[u].append(i)
        path[v].append(i)
        us.append(u)
        vs.append(v)
        chs.append(ord(ch))
    
    dis = [-1] * n
    que = [n - 1]
    dis[n - 1] = 0
    
    for u in que:
        for eid in path[u]:
            v = us[eid] ^ vs[eid] ^ u
            if dis[v] == -1:
                dis[v] = dis[u] + 1
                que.append(v)
    
    parent = [-1] * n
    
    s = []
    cur = [0]
    
    while cur[0] != n - 1:
        min_ch = 128
        for u in cur:
            for eid in path[u]:
                v = us[eid] ^ vs[eid] ^ u
                if dis[v] == dis[u] - 1:
                    min_ch = fmin(min_ch, chs[eid])
        
        s.append(min_ch)
        
        ncur = []
        for u in cur:
            for eid in path[u]:
                v = us[eid] ^ vs[eid] ^ u
                if dis[v] == dis[u] - 1 and chs[eid] == min_ch and parent[v] == -1:
                    ncur.append(v)
                    parent[v] = u
        
        cur = ncur
    
    print(len(s))
    
    ans = [n - 1]
    while ans[-1] != 0:
        ans.append(parent[ans[-1]])
    
    ans.reverse()
    print(' '.join(str(x + 1) for x in ans))
    
    print(''.join(chr(c) for c in s))