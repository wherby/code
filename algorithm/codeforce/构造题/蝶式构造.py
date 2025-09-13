# https://codeforces.com/gym/103114/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0909/solution/cf103114g.md
# algorithm/codeforce/构造题/蝶式构造 
# 实际上是对每个数字的index每一位进行编码，然后解码的过程

import init_setting
from cflibs import *
def main():
    n = II()
    pos = [0] * (n + 1)
    
    for i in range(10):
        tmp = []
        for j in range(1, n + 1):
            if j >> i & 1:
                tmp.append(j)
        
        if len(tmp):
            print(len(tmp), *tmp, flush=True)
            
            nums = LII()
            for v in nums:
                pos[v] |= 1 << i
    
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[pos[i]] = i
    
    print('!', *ans[1:])