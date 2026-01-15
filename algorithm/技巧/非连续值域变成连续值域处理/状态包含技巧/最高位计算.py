# https://codeforces.com/gym/105755/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0108/solution/cf105755c.md
# algorithm/codeforce/技巧/xor计算/testHighbit.py 
# vis[v ^ x]  v ^ x 表示 x 有哪些位为 0 ，等于求出x的补数，因为可以合并的两个数一定是大的数字的补数位置上为小的数字的最高位，  1 << bit - 1 同时记录了x的最高位的编码
# vis[v ^ x] 最终会记录 v ^ x 这个补数状态下的所有最高位的可能
# vis[j ^ (1 << i)] |= vis[j]  这里就是状态扩展， 如果 有 M 个位 为 1 的状态上有 vis[j] 的扩展， 同时M-1，M-2 的状态是M位 状态包含了M状态，所以它的状态是可以取并集   状态0 可以包含所有的状态
# 因为vis dict 里的key 是 记录数字哪些位置没用的状态，里面的1越少，说明可用的1 状态越少，同时对应的可以被插入位置是包含原数的
# dp[ni] = fmax(dp[ni], dp[i] + 1) 反向查找，从0 的的状态开始，查找当前状态可以被插入的位数，因为j 对应了某个数字它最高位是j，则进行DP







import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    
    vis = [0] * (1 << 22)
    
    for x in nums:
        bit = x.bit_length()
        v = (1 << bit) - 1
        vis[v ^ x] |= 1 << bit - 1
    
    for i in range(22):
        for j in range(1 << 22):
            if j >> i & 1:
                vis[j ^ (1 << i)] |= vis[j]
    
    dp = [0] * (1 << 22)
    
    for i in range(1 << 22):
        for j in range(22):
            if vis[i] >> j & 1:
                ni = i | (1 << j)
                dp[ni] = fmax(dp[ni], dp[i] + 1)
    
    print(max(dp))