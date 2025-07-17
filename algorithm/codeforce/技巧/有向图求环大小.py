# https://codeforces.com/problemset/problem/183/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0620/solution/cf183c.md
# 有向图一次遍历求出所有环的大小

import init_setting
from cflibs import *
def main():
    n, m = MII()
    path = [[] for _ in range(n)]

    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        path[v].append(~u)

    note = 10 ** 6
    cols = [note] * n

    ans = 0

    for i in range(n):
        if cols[i] == note:
            cols[i] = 0
            
            stk = [i]
            while stk:
                u = stk.pop()
                
                for v in path[u]:
                    if v >= 0:
                        if cols[v] == note:
                            cols[v] = cols[u] + 1
                            stk.append(v)
                        else:
                            ans = math.gcd(ans, cols[u] + 1 - cols[v])
                    else:
                        v = ~v
                        if cols[v] == note:
                            cols[v] = cols[u] - 1
                            stk.append(v)
                        else:
                            ans = math.gcd(ans, cols[u] - 1 - cols[v])

    ans = abs(ans)

    print(ans if ans else n)