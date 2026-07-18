# https://codeforces.com/gym/103306/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0713/solution/cf103306b.md
# 利用均匀分布，计算选择第K个箱子的概率分布 计算概率的前缀和
# 然后利用反向递推的放置，得到最终数字的首位的得分分布 倒推在这个分布区间计算概率

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main():
    n, m = MII()
    nums = LII()
    
    mod = 998244353
    f = Factorial(2 * 10 ** 5, mod)
    
    acc = [0] * (m + 2)
    pw = 1
    
    for i in range(m, -1, -1):
        cur = pw * f.combi(m, i) % mod
        pw = pw * (n - 1) % mod
        acc[i + 1] = cur
    
    rev_total = pow(pow(n, -1, mod), m, mod)
    
    for i in range(1, m + 2):
        acc[i] += acc[i - 1]
        acc[i] %= mod
    
    for i in range(m + 2):
        acc[i] = acc[i] * rev_total % mod
    
    ans = [0] * 10
    
    for x in nums:
        for i in range(1, 10):
            l, r = i, i
    
            for _ in range(6):
                vl = fmax(0, l - x)
                vr = fmin(m, r - x)
                
                l = l * 10
                r = r * 10 + 9
                
                if vl > vr: continue
                
                ans[i] += acc[vr + 1] - acc[vl]
                ans[i] %= mod
            
    print(*ans[1:], sep='\n')