# https://codeforces.com/gym/105190/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0808/solution/cf105190b.md
# algorithm/codeforce/dp/docs/双重循环到单层循环的DP.md
# KMP 函数能计算出当前点的最大前缀长度值是多少 
# 这里可以遍历r1,此时后面的可选l2就有n种可能值，但是从右到左看所有可能的l2,会发现 Gap+ L2 形成的值是一个单调递增函数
# ，所以从右到左遍历的时候，得到的最大值就是所有选择点的最佳值
# 因为从右到左可以维护当前函数的最佳值选择，所以从右到左遍历

import init_setting
from cflibs import *
def main():
    def prep(p):
        pi = [0] * len(p)
        j = 0
        for i in range(1, len(p)):
            while j != 0 and p[j] != p[i]:
                j = pi[j - 1]
            if p[j] == p[i]:
                j += 1
            pi[i] = j
        return pi
    
    n, x, y, z = MII()
    s = [ord(c) for c in I()]
    
    v1 = prep(s)
    
    s.reverse()
    v2 = prep(s)
    v2.reverse()
    
    ans = 0
    cur = -inf
    
    for i in range(n - 2, -1, -1):
        cur += z
        if v2[i + 1] > 0:
            cur = fmax(cur, y * v2[i + 1])
        if v1[i] > 0:
            ans = fmax(ans, cur + x * v1[i])
    
    print(ans)