# https://codeforces.com/gym/101968/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1103/solution/cf101968b.
# 如果所有矩形都相交，则所有矩形都覆盖了x,y的中位点
# 所有点对于中位点事对称分布的，所以排列个数，就只需要遍历两个象限找到个数进行象限内全排列即可

import init_setting
from cflibs import *
# Submission link: https://codeforces.com/gym/101968/submission/347061297
def main(): 
    mod = 10 ** 9 + 7
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        xs = []
        ys = []
        
        for _ in range(n * 2):
            x, y = MII()
            xs.append(x)
            ys.append(y)
        
        vxs = sorted(xs)
        vys = sorted(ys)
        
        if vxs[n] == vxs[n - 1] or vys[n] == vys[n - 1]:
            outs.append(0)
        else:
            v1 = 0
            v2 = 0
            ans = 1
            for i in range(n * 2):
                if xs[i] < vxs[n]:
                    if ys[i] < vys[n]:
                        v1 += 1
                        ans = ans * v1 % mod
                    else:
                        v2 += 1
                        ans = ans * v2 % mod
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))