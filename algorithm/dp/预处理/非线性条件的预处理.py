# https://codeforces.com/gym/105244/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0129/solution/cf105244f.md
# 对每个目标值需要的操作数是非线性的，需要预处理出每个值对应的操作数
# 对于每个物品，操作数作为重量，价值作为价值，做01背包， 但是对于背包容量固定的情况下，如果直接从背包容量计算也是可以的，但是逻辑可能更复杂一点
# 这里使用上界为12000的背包容量， 因为每个数最大操作数是12，所以n个数最大操作数是12*n， n最大1000，所以12000足够了


import init_setting
from cflibs import *
def main(): 
    n = II()
    k = II()
    
    nums = LII()
    vals = LII()
    
    ops = [1000] * 1001
    ops[0] = ops[1] = 0
    
    for i in range(1, 1001):
        for j in range(1, 1001):
            ni = i + i // j
            if ni <= 1000:
                ops[ni] = fmin(ops[ni], ops[i] + 1)
    
    dp = [0] * 12001
    
    for i in range(n):
        x = ops[nums[i]]
        y = vals[i]
        
        for j in range(12000, x - 1, -1):
            dp[j] = fmax(dp[j], dp[j - x] + y)
    
    print(max(dp[:k + 1]))