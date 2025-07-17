# https://codeforces.com/problemset/problem/260/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0626/solution/cf260d.md
# 树上的点的所有边权和记录在点上，树上的点分别为黑白色标记， 树上每条边都是不同的颜色， 把边移除，然后恢复边权满足条件
# 已知点的周围边权值。构造一个树图
# 解法是在两个不同的类中各自选一个来连接，其边权是两者最小值，再更新；类似某种图遍历

import init_setting

from cflibs import *

def main():
    n = II()
    p0 = []
    p1 = []

    for i in range(n):
        c, v = MII()
        if c: p1.append(v * n + i)
        else: p0.append(v * n + i)

    ans = []

    for _ in range(n - 1):
        v0, idx0 = divmod(p0.pop(), n)
        v1, idx1 = divmod(p1.pop(), n)
        
        if v0 <= v1 and p0:
            ans.append(f'{idx0 + 1} {idx1 + 1} {v0}')
            p1.append((v1 - v0) * n + idx1)
        else:
            ans.append(f'{idx0 + 1} {idx1 + 1} {v1}')
            p0.append((v0 - v1) * n + idx0)

    print('\n'.join(ans))

main()