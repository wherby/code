# https://codeforces.com/gym/104479/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1128/solution/cf104479d.md
# 有向无环的图，所有端点都有边，这种图也是竞赛图， 如果满足无环的特点，则它对应于一个拓扑序排列
# 因为所有边独立，所以 E(n) = E(n-1) * P(n)， P(n) 表示所有边按照正确排列的时候概率
# 递推DP 得到递推的公式 




import init_setting
from cflibs import *
def main(): 
    n, p, q = MII()
    mod = 998244353
    
    prob = p * pow(q, -1, mod) % mod
    
    dp = 1
    val = prob
    cur = 1
    
    for i in range(2, n + 1):
        dp = dp * cur % mod
        val = val * prob % mod
        cur = (cur * (1 - prob) + val) % mod
    
    print(dp)