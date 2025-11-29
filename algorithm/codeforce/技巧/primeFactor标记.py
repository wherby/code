# https://codeforces.com/gym/105561/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1125/solution/cf105561b.md
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1125/personal_submission/cf105561b_yawn_sean.py
# 这个问题先有指数部分讨论，如果非1的数组长度大于3，则所有指数部分都能满足至少19 的可能？
# 另外的难点是底数部分抽取， 如何找到一个数的最小组成质数 ：
        # for i in range(1, M + 1):
        #     cur = i
        #     val = 1
            
        #     while cur > 1:
        #         p = prime_factor[cur]
        #         val *= p
    
        #         while cur % p == 0:
        #             cur //= p
            
        #     if notes[val]:
        #         notes[i] = 1
# 如何标记一个数字的元素构成：
        # for i in range(1, M + 1):
        #     for j in range(i, M + 1, i):
        #         if notes[j]:
        #             notes[i] = 1



import init_setting
from cflibs import *
# Submission link: https://codeforces.com/gym/105561/submission/350428727
def main(): 
    n, q = MII()
    nums = LII()
    
    outs = []
    
    if n == 2:
        for _ in range(q):
            x = II()
            if pow(nums[0], nums[1], x) == 0 or pow(nums[1], nums[0], x) == 0:
                outs.append('Yes')
            else:
                outs.append('No')
    
    elif n == 3:
        for _ in range(q):
            x = II()
            flg = False
            
            for p in permutations(nums):
                a, b, c = p
                
                va = pow(a, fmin(b, 20), x)
                vb = pow(b, fmin(c, 20), x)
                
                pa = 1
                for _ in range(fmin(b, 5)):
                    pa *= a
                    pa = fmin(pa, 20)
                
                pb = 1
                for _ in range(fmin(c, 5)):
                    pb *= b
                    pb = fmin(pb, 20)
                
                if pow(va, pb, x) == 0 or pow(vb, pa, x) == 0:
                    flg = True
            
            outs.append('Yes' if flg else 'No')
    
    elif nums.count(1) >= n - 1:
        val = max(nums)
        
        for _ in range(q):
            x = II()
            outs.append('Yes' if val % x == 0 else 'No')
    
    else:
        M = 10 ** 6
        prime_factor = list(range(M + 1))
        
        for i in range(2, M + 1):
            if prime_factor[i] == i:
                for j in range(i, M + 1, i):
                    prime_factor[j] = i
        
        notes = [0] * (M + 1)
        
        for x in nums:
            notes[x] = 1
        
        for i in range(1, M + 1):
            for j in range(i, M + 1, i):
                if notes[j]:
                    notes[i] = 1
        
        for i in range(1, M + 1):
            cur = i
            val = 1
            
            while cur > 1:
                p = prime_factor[cur]
                val *= p
    
                while cur % p == 0:
                    cur //= p
            
            if notes[val]:
                notes[i] = 1
        
        for _ in range(q):
            outs.append('Yes' if notes[II()] else 'No')
    
    print('\n'.join(outs))