# 
# https://codeforces.com/gym/104848/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1021/solution/cf104848e.md
# 已知字母异位数字的gcd，求最小的数字，
# 对于大数的构造思路


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    d = {
        12: 48,
        15: 5055,
        18: 288,
        21: 7077,
        24: 8088,
        27: 3699,
        36: 48888,
        45: 5055555555,
        54: 222888888,
        63: 111888,
        72: 8088888888,
        81: 9099999999,
    }
    
    for _ in range(t):
        n = II()
        
        if len(set(str(n))) == 1:
            outs.append(n)
        elif n in d:
            outs.append(d[n])
        else:
            outs.append(-1)
    
    print('\n'.join(map(str, outs)))