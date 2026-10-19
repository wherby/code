# https://codeforces.com/gym/101915/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1014/solution/cf101915g.md
# algorithm/codeforce/图论/docs/优先DFS序构成了树节点的值域连续性.md
# 这里树上每个节点都其实对应了一段值域，使用DFS访问优先级的数节点，这样就会形成连续的节点值域
# for i in range(n - 1, 0, -1):
#     tmp_vals[i - 1] = fmin(tmp_vals[i - 1], tmp_vals[i])
# 这里是为了值域连续性做了限制，先确定可能上限，再用后一个节点限制上限

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        path = [[] for _ in range(n)]
    
        for _ in range(n - 1):
            u, v, w = MII()
            u -= 1
            v -= 1
            path[u].append(w * n + v)
            path[v].append(w * n + u)
    
        for i in range(n): path[i].sort(reverse=True)
        
        parent = [-1] * n
        vals = [0] * n
    
        tmp_vals = []    
        order = []
        stk = [0]
        
        while stk:
            u = stk.pop()
            
            tmp_vals.append(vals[u])
            order.append(u)
            
            for msk in path[u]:
                w, v = divmod(msk, n)
                if parent[u] != v:
                    parent[v] = u
                    vals[v] = fmax(vals[u], w)
                    stk.append(v)
        
        for i in range(n - 1, 0, -1):
            tmp_vals[i - 1] = fmin(tmp_vals[i - 1], tmp_vals[i])
        
        ans = 0
        for v in MII():
            ans += order[bisect.bisect_left(tmp_vals, v) - 1] + 1
        
        outs.append(f'{ans}')
    
    print('\n'.join(outs))