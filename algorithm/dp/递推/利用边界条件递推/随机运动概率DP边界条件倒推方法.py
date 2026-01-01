# https://codeforces.com/gym/104786/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1229/solution/cf104786c.md
# 这里利用方向翻转，使得到N则倒退变成了到0的时候取绝对值
# 这里从 x,y 开始DP的时候，没有办法递推，但是如果 x=0 则概率肯定为0，则这时候是边界，而且x的值一定是慢慢减少的，所以从 i=1 开始反向递推X的结果就能得到 X所有的取值
# 解题关键： 递归的边界确定，和变量单方向变化的作为外层循环的递推


import init_setting
from cflibs import *
def main(): 
    mod = 10 ** 9 + 7
    n, x, y = MII()
    
    x = n - x
    y = n - y
    
    dp = [[0] * (x + 1) for _ in range(x + 1)]
    
    rev2 = (mod + 1) // 2
    
    for i in range(1, x + 1):
        for j in range(i):
            v = dp[i - 1][abs(j - 1)]
            if j + 1 <= i - 1: v += dp[i - 1][j + 1]
            dp[i][j] = (v * rev2 + 1) % mod
    
    print(dp[x][y])