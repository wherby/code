# https://codeforces.com/gym/106020/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0629/solution/cf106020e.md
# 博弈论中奇偶性处理先手选择


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        p = [0] + LII()
        
        ans = 0
        vis = [0] * (n + 1)
        
        tmp = []
        
        for i in range(1, n + 1):
            if vis[i] == 0:
                cur = [i]
                while p[cur[-1]] != i:
                    cur.append(p[cur[-1]])
                
                for x in cur:
                    vis[x] = 1
                
                l = len(cur)
                if l % 2 == 0:
                    v = 0
                    for j in range(l):
                        if j % 2: v += cur[j]
                        else: v -= cur[j]
                    ans += abs(v)
                else:
                    v = 0
                    for j in range(1, l):
                        if j % 2: v += cur[j]
                        else: v -= cur[j]
                    
                    res = 0
                    for j in range(l):
                        if j % 2:
                            res = fmax(res, cur[j] + v)
                            v += cur[(j + 1) % l]
                            v -= cur[j]
                        else:
                            res = fmax(res, cur[j] - v)
                            v -= cur[(j + 1) % l]
                            v += cur[j]
                    
                    tmp.append(res)
        
        tmp.sort(reverse=True)
        
        for i in range(len(tmp)):
            if i % 2 == 0: ans += tmp[i]
            else: ans -= tmp[i]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))