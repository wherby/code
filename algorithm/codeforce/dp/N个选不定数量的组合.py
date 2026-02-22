# https://codeforces.com/gym/106151/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0221/solution/cf106151e.md
# 对于求取组合数量，看似会有N!的复杂度，但是对于固定的组合，可以通过损失函数找到最优排列，使得组合损失最小。从而使用排列后的顺序来进行dp，
# dp的状态转移时枚举下一个选哪个数，花费是x + y * i，因为y是和当前选了几个数相关的，所以我们需要按照y的大小来排序，先选y大的数，这样在后续的转移中，y * i的值就会更小，
# 最后我们从dp数组中找到最大的i，使得dp[i] <= b，即为答案。
# dp[i][j] 表示选了i个数，且当前状态为j的最小花费，状态转移时枚举下一个选哪个数，花费是x + y * i，
# 因为y是和当前选了几个数相关的，所以我们需要按照y的大小来排序，先选y大的数，这样在后续的转移中，y * i的值就会更小，最后我们从dp数组中找到最大的i，使得dp[i



import init_setting
from lib.cflibs import *
def main(): 
    n, b = MII()
    xs = LII()
    ys = LII()
    
    inf = 2 * 10 ** 9
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    order = sorted(range(n), key=lambda x: -ys[x])
    
    for i in range(n):
        idx = order[i]
        x = xs[idx]
        y = ys[idx]
        
        for j in range(i, -1, -1):
            dp[j + 1] = fmin(dp[j + 1], dp[j] + x + y * j)
    
    for i in range(n, -1, -1):
        if dp[i] <= b:
            print(i, dp[i])
            break