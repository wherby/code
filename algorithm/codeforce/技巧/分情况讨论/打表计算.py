# https://codeforces.com/gym/105198/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0127/solution/cf105198f.md
# 题目中给出了每个数字所需的火柴棍数量，要求用给定数量的火柴棍拼出数值最小的数字
# 通过分析得知，在大数规模情况下，填8是最优，对于小数规模，需要通过打表得到每个火柴棍数量对应的最小数字
# 因为没有前导0，所以需要分情况讨论1位数、2位数、3位数的情况进行打表
# 前导0打表处理




import init_setting
from cflibs import *

def main(): 
    digits = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    ans = [1000] * 22
    
    for i in range(10):
        ans[digits[i]] = fmin(ans[digits[i]], i)
    
    for i in range(1, 10):
        for j in range(10):
            d = digits[i] + digits[j]
            ans[d] = fmin(ans[d], i * 10 + j)
    
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                d = digits[i] + digits[j] + digits[k]
                ans[d] = fmin(ans[d], i * 100 + j * 10 + k)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        if n <= 21: outs.append(str(ans[n]))
        else:
            v = (n - 15) % 7 + 15
            outs.append(str(ans[v]) + (n - v) // 7 * '8') 
    
    print('\n'.join(outs))