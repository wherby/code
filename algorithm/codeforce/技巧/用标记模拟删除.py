# https://codeforces.com/problemset/problem/585/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0728/solution/cf585a.md
# 这里有两个模拟，队列第一个对余下的影响，因为影响受相对距离有关，所以用是否脱离队列的标记跳过脱离队列的元素
# 脱离队列的人会对后面有影响，则用累加方式记录影响，并且做脱离标记


import init_setting
from cflibs import *
def main():
    n = II()
    vs = []
    ds = []
    ps = []
    
    for _ in range(n):
        v, d, p = MII()
        vs.append(v)
        ds.append(d)
        ps.append(p)
    
    ans = []
    to_decide = [0] * n
    
    for i in range(n):
        if to_decide[i] == 0:
            ans.append(i)
            v = vs[i]
            
            for j in range(i + 1, n):
                if not to_decide[j] and v:
                    ps[j] -= v
                    v -= 1
            
            cur = 0
            for j in range(i + 1, n):
                ps[j] -= cur
                if not to_decide[j] and ps[j] < 0:
                    to_decide[j] = 1
                    cur += ds[j]
    
    print(len(ans))
    print(' '.join(str(x + 1) for x in ans))