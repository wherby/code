# https://codeforces.com/gym/106443/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0330/solution/cf106443f.md
# 计算总的分割空间数量， 和invalid 分割数量，invalid的时候，a,b,c都能大于或等于一半，所以是3倍，然后另外2个的和小于等于 n//2, 等于在n//2个格子里选择2个作为分割点



import init_setting
from cflibs import *
def main(): 
    t = II()
    mod = 10 ** 9 + 7
    
    outs = []
    
    for _ in range(t):
        n = II()
        total = (n - 1) * (n - 2) // 2 % mod
        invalid = n // 2 * (n // 2 - 1) // 2 * 3 % mod
        outs.append((total - invalid) * pow(total, -1, mod) % mod)
    
    print('\n'.join(map(str, outs)))