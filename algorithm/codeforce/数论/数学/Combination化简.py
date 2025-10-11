# https://codeforces.com/gym/104380/problem/R
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1010/solution/cf104380r.md
# Combination 组合计算化简？





import init_setting
from cflibs import *
def main():
    mod = 10 ** 9 + 7
    
    n, l, r = MII()
    nums = LII()
    
    f = Factorial(n, mod)
    
    pw2 = 1
    rev2 = (mod + 1) // 2
    
    ans = 0
    weight_left = 0
    
    for i in range(l - 1, r):
        weight_left += f.combi(n - 1, i)
        weight_left %= mod
    
    weight_right = weight_left
    
    ans += (weight_left + weight_right) * nums[0] % mod
    
    for i in range(1, n):
        pw2 = pw2 * 2 % mod
        
        weight_left = (weight_left + f.combi(n - i - 1, l - i - 1) - f.combi(n - i - 1, r - i)) % mod * rev2 % mod
        weight_right = (weight_right - f.combi(n - i - 1, l - 2) + f.combi(n - i - 1, r - 1)) % mod * rev2 % mod
        
        ans += (weight_left + weight_right) * nums[i] % mod * pw2 % mod
    
    print(ans % mod)