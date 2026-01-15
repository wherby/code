# https://codeforces.com/gym/105321/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0112/solution/cf105321e.md
# 用扰动法计算非线性变化的因子排列大小，然后DP




import init_setting
from cflibs import *
def main(): 
    n, p = MII()
    weapons = [tuple(MII()) for _ in range(n)]
    
    def cmp(weapon1, weapon2):
        a1, b1, c1 = weapon1
        a2, b2, c2 = weapon2
        
        v1 = b1 + a1 * b2
        v2 = b2 + a2 * b1
        
        if v1 < v2: return -1
        if v1 > v2: return 1
        return 0
    
    weapons.sort(key=cmp_to_key(cmp))
    
    dp = [0] * (p + 1)
    
    for a, b, c in weapons:
        for i in range(b, p + 1):
            dp[(i - b) // a] = fmax(dp[(i - b) // a], dp[i] + c)
    
    print(max(dp))