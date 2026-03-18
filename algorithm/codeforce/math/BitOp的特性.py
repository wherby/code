# https://codeforces.com/gym/106259/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0316/solution/cf106259d.md
# 求的数值是序列 的 And ， Or  的Xor结果，And只会保留全都置位的，Or会保留任一有置位的
# Xor结果就是两者的差值，所以参与的数字越小越好，这时可以用TireTree解决
# 对于求最小的Different 位的数值，一定出现在排序之后的相邻位置，这样就不用TrieTree了

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        nums.sort()
        outs.append(min(nums[i] ^ nums[i - 1] for i in range(1, n)))
    
    print('\n'.join(map(str, outs)))