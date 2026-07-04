# https://codeforces.com/gym/106607/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0702/solution/cf106607e.md
# 两个线段是关于y=x对称的，所以只有跨越这个对称轴的线段才有交点，所以去除在同一边的组合就好了



import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        ans = n * (n - 1) // 2
        
        c1 = 0
        c2 = 0
        
        for _ in range(n):
            x, y = MII()
            if x < y:
                ans -= c1
                c1 += 1
            elif x > y:
                ans -= c2
                c2 += 1
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))