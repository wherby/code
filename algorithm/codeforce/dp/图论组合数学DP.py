# https://codeforces.com/gym/106439/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0328/solution/cf106439f.md
# 原问题是n个节点 连出去的边，只有一个节点没有被连接的组合个数
# 这里采用递推，先取一个点不被连接，这时有n种取法， 取掉这个点的连接，原图可能有两种情况：
# 1， n-1 个节点没有一个节点不被连接，这时就是错排问题。使用错排递推公式解决，这时n节点可以连接 n-1个节点 algorithm/codeforce/docs/错排问题的递推公式.md
#     错排问题的边界情况，需要设置 mis[0]=1 才能得到mis[2] =1 的递推
# 2， n-1 个节点正好有一个节点不被连接，这时n节点就只能连该没有被连接的节点，这种状态也刚好是 dp[n-1]

import init_setting
from lib.cflibs import *
def main(): 
    M = 10 ** 6 + 5
    mod = 998244353
    
    mis = [0] * M
    mis[0] = 1
    for i in range(2, M):
        mis[i] = (i - 1) * (mis[i - 1] + mis[i - 2]) % mod
    
    dp = [0] * M
    for i in range(3, M):
        dp[i] = (dp[i - 1] + (i - 1) * mis[i - 1]) % mod * i % mod
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        outs.append(dp[n])
    
    print('\n'.join(map(str, outs)))