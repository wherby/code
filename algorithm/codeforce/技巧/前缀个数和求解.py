# https://codeforces.com/gym/105930/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1231/solution/cf105930e.md
# 如果在每个数字的个数计算需要增加的数字的话，这样会有 M*N 的复杂度， 如果用前缀个数和来记录的话，就可以很快得到每一个区间的最终值，这样复杂度降为 MlogN 


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        ma = max(nums)
        acc_cnt = [0] * (ma + 1)
        
        for x in nums:
            acc_cnt[x] += 1
        
        for i in range(ma):
            acc_cnt[i + 1] += acc_cnt[i]
        
        total = sum(nums) + k
        
        def check(x):
            if x >= ma: return acc_cnt[ma] * x <= total
            
            val = 0
            for i in range(0, ma + 1, x):
                l = i
                r = fmin(i + x, ma)
                val += (acc_cnt[r] - acc_cnt[l]) * (i + x)
            
            return val <= total
    
        ans = 0
        
        for i in range(1, 10 ** 6 * 2):
            if i * i > total: break
            if total % i == 0:
                if check(i): ans = fmax(ans, i)
                if check(total // i): ans = fmax(ans, total // i)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))