# https://codeforces.com/gym/106007/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1119/solution/cf106007d.md
# 把题目转换为数生成问题


import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        grid = [[-1 if c == '?' else int(c) for c in I()] for _ in range(n)]
        
        parent = [-2] * n
        parent[0] = -1
        
        que = [0]
        for u in que:
            for v in range(n):
                if grid[u][v] and parent[v] == -2:
                    parent[v] = u
                    que.append(v)
        
        if len(que) == n:
            res = []
            res.append('Yes')
            for i in reversed(que):
                if i: res.append(f'{parent[i] + 1} {i + 1}')
            outs.append('\n'.join(res))
        else:
            outs.append('No')
    
    print('\n\n'.join(outs))