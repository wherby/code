# https://codeforces.com/problemset/problem/1176/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0202/solution/cf1176c.md
# 状态机DP，记录每个数字出现的位置，然后贪心匹配最长的序列，最后计算未匹配的数字数量即为答案。
# 题目中需要找到最长的序列 4,8,15,16,23,42 的子序列，然后删除其他数字，最终答案为总长度减去最长子序列长度乘以6。
# 使用令牌桶的思想，记录每轮匹配的数字数量，每次遇到一个数字时，如果前一个数字的令牌数量大于0，则可以匹配成功，前一个数字的令牌数量减1，当前数字的令牌数量加1。
# 利用令牌传递的方式，最初0号有无限的令牌，最终6号的令牌数量即为匹配成功的序列数量。



import init_setting
from cflibs import *

def main(): 
    d = {
        4: 1,
        8: 2,
        15: 3,
        16: 4,
        23: 5,
        42: 6
    }
    
    n = II()
    nums = LII()
    
    cnt = [0] * 7
    cnt[0] = n
    
    for x in nums:
        x = d[x]
        
        if cnt[x - 1]:
            cnt[x - 1] -= 1
            cnt[x] += 1
    
    print(n - 6 * cnt[6])