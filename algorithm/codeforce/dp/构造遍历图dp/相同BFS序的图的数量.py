# https://codeforces.com/problemset/problem/1906/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/03/0328/solution/cf1906j.md

# DP(i.j)表示处理到第i个位置时候【没有遍历i的子节点前】，BFS队列入队的最后一个数字是第j个位置的值，
# 上一个状态是DP(i-1,j1) 这时 i-1个节点必须连接 j1...j 的节点，并且这些节点是递增的
# DP(i,j) = sum(pow(2**(j-i+1) * dp[i-1][jt])) j1<=jt<=j 因为这时，第i个节点可以连接或者不连所有已经在队列里的节点 有 pow(2,j-i-1)种选择
# 在每次遍历 i的时候， 因为 DP(i,j) 求 j1,,j的前缀和，所以可以用acc表示此前缀和，
# 其中j1的值可以根据 prev 数组求出，
# 当 i 比较小的时候， j 也不能取很大的值，但是在循环的时候不用关心，
# 当 prev[j] 比i还小的时候，因为acc的值是用i-1开始加的，所以也可以直接减去，不用考虑
# 最终 DP 的值，DP(n-1) 在i = n-1 的时候肯定能取到， 但是计算acc的时候，i-1开始的， i-1之前的值其实如果需要求前缀已经在dp[i-1]已经记录了
# 最终的 DP[n-1]的值， 包含了 dp[1][n] --- dp[n][n]的所有可能的值 

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    nums = LII()

    mod = 998244353

    prev = list(range(n))
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            prev[i] = prev[i - 1]

    dp = [0] * n
    acc = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n):
        pw = 1
        for j in range(i - 1, n):
            acc[j + 1] = (pw * dp[j] + acc[j]) % mod
            pw = pw * 2 % mod
        
        for j in range(i, n):
            dp[j] = (acc[j + 1] - acc[fmax(prev[j] - 1, 0)]) % mod
        
        for j in range(n + 1):
            acc[j] = 0

    print(dp[n - 1])



