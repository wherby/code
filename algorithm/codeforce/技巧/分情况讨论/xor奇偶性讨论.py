# https://codeforces.com/gym/103451/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0209/solution/cf103451i.md
# 题目中按位分析 and or xor 的值域，分析每个位置的操作数，判断是否能满足奇偶要求
# 如果 and 位为 1，则 or 位和 xor 位必须相同，且 n 的奇偶性必须与 xor 位相同
# 如果 and 位为 0，or 位为 0，则 xor 位必须为 0
# 如果 and 位为 0，or 位为 1，则如果 n >= 2,则 满足xor的条件只有奇偶性一致的情况才成立，奇偶性一致则空间为 2^(n-1)，
#                                           如果 xor 位为 0，，则还要减去全为 0 的情况 (因为和or必须为1 冲突)
#                                           如果 xor 为1 ， 如果 n 的奇偶性与 xor 位相同，则还要减去全为 1 的情况 (因为和and必须为0 冲突)      

import init_setting
from cflibs import *

def main(): 
    n = II()
    and_val = [int(c) for c in I()]
    or_val = [int(c) for c in I()]
    xor_val = [int(c) for c in I()]
    
    k = len(and_val)
    
    ans = 1
    mod = 10 ** 9 + 7
    
    saved = pow(2, n - 1, mod)
    
    for i in range(k):
        res = 0
        
        if and_val[i]:
            if or_val[i] and n % 2 == xor_val[i]:
                res = 1
        else:
            if or_val[i] == 0:
                if xor_val[i] == 0:
                    res = 1
            else:
                if n >= 2:
                    res = saved
                    if xor_val[i] == 0:
                        res -= 1
                        res %= mod
                    if n % 2 == xor_val[i]:
                        res -= 1
                        res %= mod
        
        ans = ans * res % mod
    
    print(ans)