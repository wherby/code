# https://codeforces.com/gym/106179/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1111/solution/cf106179d.md
# 原题是需要 subseqence 来获取，高数字放高位，或者高数字放低位的两个数组，就能一次消去，所以用数位的异或关系就可以分离两种不同的数列


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        v1 = []
        v2 = []
        
        for i in range(n):
            if (i < n // 2) ^ (nums[i] <= n // 2):
                v1.append(nums[i])
            else:
                v2.append(nums[i])
        
        if len(v1) and len(v2):
            outs.append('2')
            outs.append(f'{len(v1)} {" ".join(map(str, v1))}')
            outs.append(f'{len(v2)} {" ".join(map(str, v2))}')
        else:
            outs.append('1')
            outs.append(f'{n} {" ".join(map(str, nums))}')
    
    print('\n'.join(outs))

main()