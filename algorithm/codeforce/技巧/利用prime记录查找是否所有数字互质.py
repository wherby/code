# https://codeforces.com/gym/105408/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1018/solution/cf105408g.md
# prime_factor 会记录每个数字最大的prime因子
# 利用 prime_factor 来因数分解所有的数字，如果prime 因子出现2次，则证明不是互质


import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    g = math.gcd(*nums)
    
    for i in range(n):
        nums[i] //= g
    
    M = max(nums)
    prime_factor = list(range(M + 1))
    
    for i in range(2, M + 1):
        if prime_factor[i] == i:
            for j in range(i, M + 1, i):
                prime_factor[j] = i
    
    vis = [0] * (M + 1)
    
    for x in nums:
        while x > 1:
            p = prime_factor[x]
            if vis[p]: exit(print('NO'))
            vis[p] = 1
            while x % p == 0:
                x //= p
    
    print('YES')