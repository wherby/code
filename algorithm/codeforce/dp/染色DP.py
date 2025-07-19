# 
# https://codeforces.com/problemset/problem/111/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0719/solution/cf111d.md
# 这里两边的集合数量相等，所以中间的集合数字假设为 i, 中间的颜色一定是两边的交集， 这时再从两边各取 j-i 个不同的元素，就可以得到所有颜色的组合
# fac.comb(k, i) * fac.comb(k - i, 2 * (j - i)) % mod * fac.comb(2 * (j - i), j - i) % mod  ： 先取中间的i个相同元素，然后在余下的元素里取 2*(j-i) 作为两边特别元素，再把一半分给一边，完成了两边 j 中间i 种元素的分配


import init_setting
from cflibs import *
from lib.combineWithPreCompute import *
def main():
    n, m, k = MII()
    mod = 10 ** 9 + 7
    fac = Factorial(10 ** 6, mod)
    
    if m == 1:
        print(pow(k, n, mod))
        exit()
    
    dp = [0] * (n + 1)
    
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            dp[j] = (dp[j - 1] + j * dp[j]) % mod
        dp[0] = 0
    
    for i in range(n + 1):
        dp[i] = dp[i] * fac.fact(i) % mod
    
    ans = 0
    for i in range(n + 1):
        val = pow(i, n * (m - 2), mod)
        for j in range(i, n + 1):
            ans += fac.comb(k, i) * fac.comb(k - i, 2 * (j - i)) % mod * fac.comb(2 * (j - i), j - i) % mod * dp[j] % mod * dp[j] % mod * val % mod
            if ans >= mod:
                ans -= mod
    
    print(ans)

main()