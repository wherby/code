# https://codeforces.com/gym/105387/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0922/solution/cf105387g.md
# 这里所有转移是不限制的，
# if i > kr + 1: dpr[i] -= dpg[i - kr - 1] + dpb[i - kr - 1]
#     elif i == kr + 1: dpr[i] -= 1
# 这里红色转移，只减去了 kr-1回合从其他颜色转移过来的方块，为什么不减去红色有kr的方块呢？
# 假设前一个状态有Kr个红色方块存在了，那Kr个方块的前一个方块是什么颜色呢？如果前一个方块是红色，就和刚好有Kr个方块矛盾，则前一个方块是其他颜色，就是上面的减法，
# 但是有一个特殊情况，就是在Kr+1的时候，前面kr个方块都是红色，再前面没有方块，在kr+1这个位置就要减去1

import init_setting
from cflibs import *

def main():
    n, kr, kg, kb = MII()
    
    dpr = [0] * (n + 1)
    dpg = [0] * (n + 1)
    dpb = [0] * (n + 1)
    
    dpr[1] = 1
    dpg[1] = 1
    dpb[1] = 1
    
    mod = 10 ** 9 + 7
    
    for i in range(2, n + 1):
        total = dpr[i - 1] + dpg[i - 1] + dpb[i - 1]
        
        dpr[i] = total
        if i > kr + 1: dpr[i] -= dpg[i - kr - 1] + dpb[i - kr - 1]
        elif i == kr + 1: dpr[i] -= 1
        
        dpg[i] = total
        if i > kg + 1: dpg[i] -= dpr[i - kg - 1] + dpb[i - kg - 1]
        elif i == kg + 1: dpg[i] -= 1
        
        dpb[i] = total
        if i > kb + 1: dpb[i] -= dpr[i - kb - 1] + dpg[i - kb - 1]
        elif i == kb + 1: dpb[i] -= 1
        
        dpr[i] %= mod
        dpg[i] %= mod
        dpb[i] %= mod
        
    
    print((dpr[n] + dpg[n] + dpb[n]) % mod)