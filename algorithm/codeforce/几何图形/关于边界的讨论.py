# https://codeforces.com/gym/102416/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0609/solution/cf102416e.md
# 题意里边界上的点可能不是被覆盖的点，在求面积的时候，边界上的点是特殊的点。。
# 题目中有隐含最少选择的需求？ 所以要用三倍扩大之后的范围去排除


import init_setting
from lib.cflibs import *
def main():
    n = II()
    xs = []
    ys = []
    zs = []
    rs = []
    
    for _ in range(n):
        x, y, z, r = MII()
        xs.append(x)
        ys.append(y)
        zs.append(z)
        rs.append(r)
    
    ans = []
    for i in sorted(range(n), key=lambda x: -rs[x]):
        flg = True
        
        for j in ans:
            dx = xs[j] - xs[i]
            dy = ys[j] - ys[i]
            dz = zs[j] - zs[i]
            totr = rs[j] * 3 - rs[i]
            
            if dx * dx + dy * dy + dz * dz < totr * totr:
                flg = False
        
        if flg:
            ans.append(i)
    
    print(len(ans))
    print(*(x + 1 for x in ans))