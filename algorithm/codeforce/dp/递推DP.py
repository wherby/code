# https://codeforces.com/problemset/problem/1957/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0822/solution/cf1957c.md
# 一个n*n的棋盘，怎么考虑成一维的DP？
# 从大到小： 因为每一行一列都只能放一个棋子，则第一行，一定会放置一个棋子，如果放置在对角线上，则变成了f(n-1)的问题，如果放置在第一行，第一列的其他位置，则有 2*(n-1)*f(n-2)种 情况
# 从小到大： 从小的状态到大的状态有2种增加方式，一个是添加到新的对角线方向，一种是添加在对角线外的其他点

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    dp = [0] * (3 * 10 ** 5 + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, 3 * 10 ** 5 + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % mod
    
    for _ in range(t):
        n, k = MII()
        for _ in range(k):
            x, y = MII()
            if x == y: n -= 1
            else: n -= 2
        outs.append(dp[n])
    
    print('\n'.join(map(str, outs)))