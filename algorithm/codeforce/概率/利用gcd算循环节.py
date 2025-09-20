# https://codeforces.com/gym/105862/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0917/solution/cf105862h.md
# 利用gcd计算循环节的大小，由于所有点都可以作为起点，循环节大小就是平均次数

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        total = sum(nums)
        times = 0
        for i in range(n):
            g = math.gcd(n, i)
            times += n // g
        
        rev_n = pow(n, -1, mod)
        outs.append(sum(nums) * times % mod * rev_n % mod * rev_n % mod)
    
    print('\n'.join(map(str, outs)))