# https://codeforces.com/gym/104974/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0619/solution/cf104974n.md
# algorithm/codeforce/math/docs/高维状态空间投影.md
# 这里需要知道分组的成员完全没有挨着的情况，为了计算这个情况使用了二项式反演，计算 至少0，1,2,3，N//2 对捆绑的情况，但是容斥原理，相邻项需要取相反的符合
# 而捆绑的时候，把两个数字当成了一个数字，这里少算了这两个数字不同方向的情况，所以需要把不同方向也考虑进去，
# 这时就形成了符合相邻情况的所有组合了，怎么求组内方向一定的组合呢？
# 这时可以假设所有组内方向的情况是一定的，因为前面计算的情况包含了所有组内的情况，所以，可以把组内分布空间相除，得到组内分布的基情况？
# 然后乘以符合题意的多少个是正方向的分布
# 这里可以知道，在求高维组合的时候，把一个限制去掉了，因为该限制所生成的分布是均匀分布的，再后面可以算出基量然后乘以符合该分布的组合数


import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main():
    n, d = MII()
    mod = 998244353
    
    f = Factorial(n, mod)
    pw2 = [1] * (n + 1)
    for i in range(n):
        pw2[i + 1] = pw2[i] * 2 % mod
    
    ans = 0
    
    for i in range(n // 2 + 1):
        ans += (1 if i % 2 == 0 else -1) * f.fac(n - i) * f.combi(n // 2, i) % mod * pw2[i] % mod
        ans %= mod
    
    ans = ans * pow(pw2[n // 2], -1, mod) % mod
    
    if (n // 2 - d) % 2: print(0)
    else: print(ans * f.combi(n // 2, (n // 2 + d) // 2) % mod)