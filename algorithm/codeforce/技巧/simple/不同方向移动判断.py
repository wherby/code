# https://codeforces.com/problemset/problem/131/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0807/solution/cf131e.md
# 象的各个方向移动判定

import init_setting
from cflibs import *
def main():
    n, m = MII()
    
    xs = []
    ys = []
    
    for _ in range(m):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    cnt = [0] * m
    
    tmp = [[] for _ in range(2 * n + 1)]
    
    for i in range(2 * n + 1):
        tmp[i].clear()
    
    for i in range(m):
        tmp[xs[i]].append(i)
    
    for i in range(2 * n + 1):
        tmp[i].sort(key=lambda x: ys[x])
        
        for j in range(1, len(tmp[i])):
            cnt[tmp[i][j]] += 1
            cnt[tmp[i][j - 1]] += 1
    
    for i in range(2 * n + 1):
        tmp[i].clear()
    
    for i in range(m):
        tmp[ys[i]].append(i)
    
    for i in range(2 * n + 1):
        tmp[i].sort(key=lambda x: xs[x])
        
        for j in range(1, len(tmp[i])):
            cnt[tmp[i][j]] += 1
            cnt[tmp[i][j - 1]] += 1
    
    for i in range(2 * n + 1):
        tmp[i].clear()
    
    for i in range(m):
        tmp[xs[i] + ys[i]].append(i)
    
    for i in range(2 * n + 1):
        tmp[i].sort(key=lambda x: xs[x])
        
        for j in range(1, len(tmp[i])):
            cnt[tmp[i][j]] += 1
            cnt[tmp[i][j - 1]] += 1
    
    for i in range(2 * n + 1):
        tmp[i].clear()
    
    for i in range(m):
        tmp[xs[i] - ys[i]].append(i)
    
    for i in range(2 * n + 1):
        tmp[i].sort(key=lambda x: xs[x])
        
        for j in range(1, len(tmp[i])):
            cnt[tmp[i][j]] += 1
            cnt[tmp[i][j - 1]] += 1
    
    ans = [0] * 9
    for x in cnt:
        ans[x] += 1
    
    print(*ans)