# https://codeforces.com/gym/106251/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1225/solution/cf106251g.md
# 构造进位技巧 如果 A + B = C ,A 和C 的数字一样, 构造技巧就是利用 X *Base -X == B 构造数字, X 的各位数字又由 B的数字决定  
# A与C 的数码一致,则他们的差一定可以整除(Base-1), 那A就等于 B//(Base -1)  


import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, b = MII()
        nums = LII()
        
        if sum(nums) % (b - 1): outs.append('NO')
        else:
            outs.append('YES')
            
            res = []
            
            cur = 0
            for x in nums:
                cur = cur * b + x
                res.append(cur // (b - 1))
                cur %= b - 1
            
            outs.append(str(n + 2))
            outs.append('1 0 ' + ' '.join(map(str, res)))
            outs.append('1 ' + ' '.join(map(str, res)) + ' 0')
    
    print('\n'.join(outs))