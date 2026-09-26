# https://codeforces.com/gym/106710/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0918/solution/cf106710e.md
# 子问题：  有 2**（n-1)个数字，每个数字从1到k 种选取，求递增排列的数目
# 这里需要知道有序数组的组合数量是多少
# 由于有序数组是非递减的，从组合数来看会有连续项相等的情况，这时把数字和index加在一起就变成了一个严格递增的数组
# 这时有序数量和从 1 到 k +(2**(n-1))-1 个数字中选择 2**（n-1)数字的组合数一一对应了 



import init_setting
from cflibs import *
def main():
    n, k = MII()
    mod = 998244353
    
    ans = 0
    cur_len = 1
    cur_len1 = 1
    
    for _ in range(n):
        cur_len = cur_len * 2 % mod
        cur_len1 = cur_len1 * 2 % (mod - 1)
        
        a = 1
        b = pow(k, cur_len1, mod)
        
        for i in range(1, k):
            a = a * (k + cur_len - i) % mod
            b = b * i % mod
        
        prob = (mod + 1 - a * pow(b, -1, mod) % mod) % mod
        
        ans = (ans + prob) % mod
    
    print(ans)