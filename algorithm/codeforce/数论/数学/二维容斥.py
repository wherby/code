# https://codeforces.com/gym/104015/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1101/solution/cf104015g.md
# 求两个方向的或集合
# algorithm/codeforce/数论/数学/二维容斥
# 原题求两个维度满足其中之一的数量
# 首先用容斥，在每个维度满足条件的数量 减去都满足的数量
# F= A + B -C  A,B: 各个维度单独满足的数量 C :两个维度都满足的数量  
# 然后我们，要求两个维度都满足的数量，也用容斥原理： 即总的数量减去 两个维度分别不满足的数量， 再加上两个维度同时不满足的数量
# C= all - notA -notB + notAAndnotB 
# notA 可能有2同和三同的两种情况
# notAandnotB则只有 2同的情况， 因为其中 “there are no two problems that have the same topic and difficulty at the same time.” 
# 所以  (cnt1[xs[i]] - 1) * (cnt2[ys[i]] - 1) 不会产生3同的情况





import init_setting
from cflibs import *
def main(): 
    M = 2 * 10 ** 5
    n = II()
    
    cnt1 = [0] * M
    cnt2 = [0] * M
    
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = GMI()
        cnt1[x] += 1
        cnt2[y] += 1
        xs.append(x)
        ys.append(y)
    
    total = 0
    
    dp0, dp1, dp2, dp3 = 1, 0, 0, 0
    for x in cnt1:
        dp3 += dp2 * x
        dp2 += dp1 * x
        dp1 += dp0 * x
    
    total += dp3
    
    dp0, dp1, dp2, dp3 = 1, 0, 0, 0
    for x in cnt2:
        dp3 += dp2 * x
        dp2 += dp1 * x
        dp1 += dp0 * x
    
    total += dp3
    
    dup = math.comb(n, 3)
    
    for v in cnt1:
        dup -= math.comb(v, 2) * (n - v)
    
    for v in cnt2:
        dup -= math.comb(v, 2) * (n - v)
    
    for i in range(n):
        dup += (cnt1[xs[i]] - 1) * (cnt2[ys[i]] - 1)
    
    for v in cnt1: dup -= math.comb(v, 3)
    for v in cnt2: dup -= math.comb(v, 3)
    
    print(total - dup)