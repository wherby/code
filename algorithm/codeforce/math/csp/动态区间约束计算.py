# https://codeforces.com/gym/102465/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0307/solution/cf102465e.md
# 每个数字有一定的区间区域，同时这些区间区域的和要满足一个约束，就是区间和能构成100%的比例
# 所以这里是一个动态区间约束计算的问题，首先我们要计算出每个数字的区间范围，然后根据这些区间范围来计算出每个数字的最小值和最大值 
# algorithm/codeforce/math/csp/index.md


import init_setting
from cflibs import *
def main(): 
    n = II()
    names = []
    scores = []
    others = []
    
    for _ in range(n):
        x, y = LI()
        names.append(x)
        y = int(y)
        
        if y == 0:
            scores.append(0)
            others.append(49)
        elif y == 100:
            scores.append(9950)
            others.append(50)
        else:
            scores.append(y * 100 - 50)
            others.append(99)
    
    total = sum(scores)
    total_other = sum(others)
    
    if total > 10000 or total + total_other < 10000:
        print('IMPOSSIBLE')
    else:
        resid = 10000 - total
        
        for i in range(n):
            mi = scores[i] + fmax(0, resid - (total_other - others[i]))
            ma = scores[i] + fmin(others[i], resid)
    
            print(f'{names[i]} {mi // 100}.{mi % 100:02d} {ma // 100}.{ma % 100:02d}')