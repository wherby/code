# https://codeforces.com/problemset/problem/60/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0530/solution/cf60c.md
# 试填每个联通区域的某一个值，并且记录所有影响的值，如果失败则恢复原始值
# 因为数据范围是10**6， 则可以枚举 10**3 用除数枚举另一半可能性

import init_setting
from cflibs import *
def main():
    n, m = MII()

    us = [0] * m
    vs = [0] * m
    gcds = [0] * m
    lcms = [0] * m

    path = [[] for _ in range(n)]

    for i in range(m):
        us[i], vs[i], gcds[i], lcms[i] = MII()
        us[i] -= 1
        vs[i] -= 1
        path[us[i]].append(i)
        path[vs[i]].append(i)

    ans = [-1] * n

    for i in range(n):
        if ans[i] == -1:
            if len(path[i]) == 0:
                ans[i] = 1
                continue
            
            total_flg = False
            
            cur_l = 0
            for eid in path[i]:
                cur_l = math.gcd(cur_l, lcms[eid])
            
            for x in range(1, 1001):
                if cur_l % x == 0:
                    f = x
                    flg = True
                    
                    ans[i] = f
                    
                    stk = [i]
                    tmp = [i]
                    
                    
                    while stk:
                        u = stk.pop()
                        
                        for eid in path[u]:
                            v = us[eid] + vs[eid] - u
                            g = gcds[eid]
                            l = lcms[eid]
                            
                            if ans[u] == 0: break
                            
                            if ans[v] == -1:
                                ans[v] = g * l // ans[u]
                                tmp.append(v)
                                stk.append(v)
                            
                            if math.gcd(ans[u], ans[v]) != g or ans[u] * ans[v] != g * l:
                                flg = False
                                break
                    
                    if flg:
                        total_flg = True
                        break
                    
                    for u in tmp:
                        ans[u] = -1
                    
                    f = cur_l // x
                    flg = True
                    
                    ans[i] = f
                    
                    stk = [i]
                    tmp = [i]
                    
                    while stk:
                        u = stk.pop()
                        
                        for eid in path[u]:
                            v = us[eid] + vs[eid] - u
                            g = gcds[eid]
                            l = lcms[eid]
                            
                            if ans[u] == 0: break
                            
                            if ans[v] == -1:
                                ans[v] = g * l // ans[u]
                                tmp.append(v)
                                stk.append(v)

                            if math.gcd(ans[u], ans[v]) != g or ans[u] * ans[v] != g * l:
                                flg = False
                                break
                    
                    if flg:
                        total_flg = True
                        break
                    
                    for u in tmp:
                        ans[u] = -1

            if not total_flg:
                exit(print('NO'))

    print('YES')
    print(*ans)