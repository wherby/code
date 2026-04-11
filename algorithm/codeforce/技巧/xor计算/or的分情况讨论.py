# https://codeforces.com/gym/106007/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0409/solution/cf106007l.md
# 需要 or 操作数字使得数字一致，
# 需要求解 当前所有数字的or值，和or值与 当前所有数字and值的差，就是必须置位的值
# 这时分情况讨论x 是否能达成使得数字统一： 
# 1. 如果 x 不包含必要值，则必不成功
# 2. 如果 x 不会引入新的置位，， x & total_or == x ，则操作次数可以通过贪心求得
# 3. 如果 x 引入了新的置位，所有的数字都需要操作，则操作次数和n有关



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        nums = LII()
        
        total_or = reduce(ior, nums)
        op_must = 0
        
        ans = 0
        cur = -1
        
        for i in range(n):
            if nums[i] != total_or:
                op_must |= total_or - nums[i]
                if i > cur:
                    ans += 1
                    cur = i + m - 1
        
        q = II()
        for _ in range(q):
            x = II()
            if x & op_must != op_must: outs.append(-1)
            elif x & total_or == x or ans == 0: outs.append(ans)
            else: outs.append((n - 1) // m + 1)
    
    print('\n'.join(map(str, outs)))