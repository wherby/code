# https://codeforces.com/gym/106457/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0407/solution/cf106457d.md
# 利用均摊算法，连续x 上的上下凸包变化最多是2y,所以可以上下搜索
# algorithm/geometry/边界线求面积/离散格点凸包性质.md  利用已知凸包端点，设置上下边界的bound，避免在某个x值的时候因为离散格点性质没有标记让上下搜索跑飞
# 利用皮克定理，求面积 algorithm/geometry/边界线求面积/皮克定理中-1.md


import init_setting
from lib.cflibs import *
def main(): 
    d = {
        'X': 0,
        'P': 1,
        'I': 2
    }
    
    def query(x, y):
        print('?', x, y, flush=True)
        return d[I()]
    
    n, t, b = MII()
    
    ans = [[0] * (n + 1) for _ in range(n + 1)]
    l, r = t, t
    
    for i in range(1, n + 1):
        ans[1][i] = query(1, i)
        ans[n][i] = query(n, i)
        if ans[1][i]:
            l = fmin(l, i)
            r = fmax(r, i)
    
    for i in range(2, n):
        l_bound = (t - b) * (i - 1) // (n - 1) + b
        r_bound = ((t - b) * (i - 1) - 1) // (n - 1) + b
        ans[i][l] = query(i, l)
        
        if ans[i][l]:
            while l > 1:
                l -= 1
                ans[i][l] = query(i, l)
                if ans[i][l] == 0 or l > l_bound:
                    l += 1
                    break
        else:
            while l < l_bound:
                l += 1
                ans[i][l] = query(i, l)
                if ans[i][l]:
                    break
        
        ans[i][r] = query(i, r)
        
        if ans[i][r]:
            while r < n:
                r += 1
                ans[i][r] = query(i, r)
                if ans[i][r] == 0:
                    r -= 1
                    break
        else:
            while r > r_bound:
                r -= 1
                ans[i][r] = query(i, r)
                if ans[i][r]:
                    break
        
        for j in range(l + 1, r):
            ans[i][j] = 2
    
    print('!', sum(sum(x) for x in ans) - 2, end='')
main()