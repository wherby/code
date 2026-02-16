# https://codeforces.com/problemset/problem/2195/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0216/solution/cf2195f.md
# 观察题意，发现满足条件的点对是满足二次不等式的点对，且满足条件的点对之间的关系也是满足二次不等式的点对，所以可以先按照 z 坐标排序，然后分别从前往后和从后往前进行动态规划，
# 来求出以每个点为结尾和以每个点为开头的最长满足条件的序列长度，最后相加减去 1 就是以该点为中间点的最长满足条件的序列长度了
# 如果两个方程没有解，则两条曲线不相交，因为是和x=0 即 y轴的交点排序的，所以不相交的性质具有传递性，所以可以认为是一条链，满足条件的点对之间的关系也是满足条件的点对，所以可以用动态规划求出最长链的长度了


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        xs = []
        ys = []
        zs = []
        
        for _ in range(n):
            x, y, z = MII()
            xs.append(x)
            ys.append(y)
            zs.append(z)
        
        st_range = sorted(range(n), key=lambda x: zs[x])
        
        dp_pref = [1] * n
        
        for i in range(n):
            for j in range(i):
                vi = st_range[i]
                vj = st_range[j]
                
                if xs[vi] == xs[vj]:
                    if ys[vi] == ys[vj]:
                        dp_pref[vi] = fmax(dp_pref[vi], dp_pref[vj] + 1)
                else:
                    a = xs[vi] - xs[vj]
                    b = ys[vi] - ys[vj]
                    c = zs[vi] - zs[vj]
                    
                    if b * b < 4 * a * c:
                        dp_pref[vi] = fmax(dp_pref[vi], dp_pref[vj] + 1)
        
        dp_suff = [1] * n
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                vi = st_range[i]
                vj = st_range[j]
                
                if xs[vi] == xs[vj]:
                    if ys[vi] == ys[vj]:
                        dp_suff[vi] = fmax(dp_suff[vi], dp_suff[vj] + 1)
                else:
                    a = xs[vi] - xs[vj]
                    b = ys[vi] - ys[vj]
                    c = zs[vi] - zs[vj]
                    
                    if b * b < 4 * a * c:
                        dp_suff[vi] = fmax(dp_suff[vi], dp_suff[vj] + 1)
        
        outs.append(' '.join(str(x + y - 1) for x, y in zip(dp_pref, dp_suff)))
    
    print('\n'.join(map(str, outs)))