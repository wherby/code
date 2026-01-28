# https://codeforces.com/gym/105125/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0126/solution/cf105125b.md
# 题目中奇偶操作的时候对应的值域确定，和总操作次数有关
# 通过分析每个位置的操作数，判断是否能满足奇偶要求
# 然后构造出一个满足要求的操作序列即可，贪心地在能操作的位置交替进行奇偶操作，构造的时候使用堆栈确定1的位置

import init_setting
from cflibs import *

def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        op_total = sum(nums)
        op_step2 = sum(fmax(v - 1, 0) for v in nums)
        
        if op_total % 2 == 0: outs.append('NO')
        elif op_step2 < op_total - op_step2 - 1: outs.append('NO')
        else:
            outs.append('YES')
            
            st_range = sorted([i for i in range(n) if nums[i]], key=lambda x: nums[x])
            
            ones = []
            ops = []
            
            pt = 0
            flg = 1
            k = len(st_range)
            
            for _ in range(sum(nums)):
                while pt < k and nums[st_range[pt]] == 1:
                    ones.append(st_range[pt])
                    pt += 1
                
                if flg and ones:
                    idx = ones.pop()
                    nums[idx] -= 1
                    ops.append(idx)
                else:
                    nums[st_range[pt]] -= 1
                    ops.append(st_range[pt])
                
                flg ^= 1
            
            outs.append(' '.join(str(x + 1) for x in ops))
    
    print('\n'.join(outs))