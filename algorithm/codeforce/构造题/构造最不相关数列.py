# https://codeforces.com/gym/105870/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1217/solution/cf105870a.md
# 构造两个数列由相同数字组成，无论怎么循环移动，其中的LCS 为 C+1， C是初始数组中最大相同元素数量

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        nums.sort(reverse=True)
        
        cnt = Counter()
        tmp = [[] for _ in range(n)]
        
        for x in nums:
            tmp[cnt[x]].append(x)
            cnt[x] += 1
        
        ans = []
        for v in tmp:
            ans += v
        
        nums.reverse()
        
        outs.append(' '.join(map(str, nums)))
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))