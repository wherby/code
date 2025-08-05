# https://codeforces.com/problemset/problem/319/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0728/solution/cf319b.md
# 要知道一个点可以被消除多少次，或者在第几次被消除，只能从左到右遍历模拟过程才能知道
# 从右到左，维护一个非递增的单调栈，则新的元素来消去栈里的元素则会增加一次消去值。
# 如果从右到左，利用单调栈，则栈里的元素可以知道它可以消除多少次[如果没有被左边元素消除的情况下]，如果它被左边的元素消除，则左边的元素可以继承它剩余的次数
# stack 里剩余的元素代表从右到左子序列最后阶段的状态，dp值表示子序列阶段中每个元素的值，但是这个值不是下一个阶段的时候的值，但是会参与阶段转移，就是DP
# 


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    dp = [0] * n
    stk = []
    
    for i in range(n - 1, -1, -1):
        res = 0
        while stk and nums[stk[-1]] < nums[i]:
            res = fmax(res + 1, dp[stk.pop()])
        
        stk.append(i)
        dp[i] = res
    
    print(max(dp))