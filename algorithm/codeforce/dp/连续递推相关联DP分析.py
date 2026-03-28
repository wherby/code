# https://codeforces.com/gym/106439/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0327/solution/cf106439n.md
# 按照题意递推的时候，如果是0的时候，i 连接  i-1, 则此时转移贡献分量为 dp[i-1] + 2**(i-2)
# 如果是1的时候， i 连接 i-2, 高度贡献值为 H(i-2) + 2**(i-2), 但是这时要分析， dp[i-2]的时候，只有i-2个元素构成的空间，但是第i个节点选1的时候，空间是 i-1个元素
# 此时 H(i-2) = dp[i-2]*2, 2 表示i-1位可以选0，或者选1，使得空间倍增

import init_setting
from cflibs import *
def main(): 
    M = 2 * 10 ** 5 + 5
    mod = 10 ** 9 + 7
    
    pw2 = [1] * M
    dp = [0] * M
    
    for i in range(1, M):
        pw2[i] = pw2[i - 1] * 2 % mod
    
    dp[1] = 1
    
    for i in range(2, M):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2] + pw2[i - 1]) % mod
    
    t = II()
    outs = []
    
    for _ in range(t):
        outs.append(dp[II()])
    
    print('\n'.join(map(str, outs)))