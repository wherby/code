# https://codeforces.com/gym/102201/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0908/solution/cf102201a.md
# 要求相等的时候，乘法相对于另一个偶数数字做除法
# 对于奇数的处理，用凑偶数的方式解决，


import init_setting
from cflibs import *
def main():
    a, b = MII()
    
    ops = []
    
    while a != b:
        if a % 2 == 0:
            ops.append('B+=B')
            a //= 2
        elif b % 2 == 0:
            ops.append('A+=A')
            b //= 2
        elif a > b:
            ops.append('A+=B')
            ops.append('B+=B')
            a += b
            a //= 2
        else:
            ops.append('B+=A')
            ops.append('A+=A')
            b += a
            b //= 2
    
    print(len(ops))
    print('\n'.join(ops))