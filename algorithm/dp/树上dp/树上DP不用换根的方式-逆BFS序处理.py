# https://codeforces.com/gym/106164/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0515/solution/cf106164g.md
# 这里树上查找两个最大值的点，其中树上路径使用逆BFS序处理树上DP algorithm/dp/树上dp/逆BFS序遍历处理DP.md
# 另外的曼哈顿距离最大值点，采用状态展开的方式，求解任意两点的最大曼哈顿距离  algorithm/mathA/abs/最大曼哈顿距离求解.md



import init_setting
from cflibs import *
def main():  
    n = II()
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v, w = MII()
        u -= 1
        v -= 1
        path[u].append(w * n + v)
        path[v].append(w * n + u)
    
    pts = [[] for _ in range(3)]
    
    for _ in range(n):
        pt = LII()
        
        for i in range(3):
            pts[i].append(pt[i])
    
    parent = [-1] * n
    que = [0]
    
    for u in que:
        for msk in path[u]:
            v = msk % n
            if parent[u] != v:
                parent[v] = u
                que.append(v)
    
    ans = 0
    
    ma = [[0] * n for _ in range(8)]
    
    for i in reversed(que):
        for j in range(8):
            for k in range(3):
                if j >> k & 1:
                    ma[j][i] += pts[k][i]
                else:
                    ma[j][i] -= pts[k][i]
        
        for msk in path[i]:
            w, v = divmod(msk, n)
            if parent[v] == i:
                for j in range(8):
                    ans = fmax(ans, ma[j][v] + w + ma[7 - j][i])
                for j in range(8):
                    ma[j][i] = fmax(ma[j][i], ma[j][v] + w)
    
    print(ans)