# https://codeforces.com/gym/103347/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0207/solution/cf103347j.md
# 原题中 k*(x**k) === y(mod p) 其中 k 是未知数，x,y,p,a 是已知数
# x**k 是一个独立的循环数组，且 k* [独立循环数组]， 本来 k*一个固定的数字的循环长度为p ,
# 但是两个循环周期叠加就变成了 k*p 
# 为了求解，利用费马小定理，求出 x 的逆元，得到 k* [独立循环数组] 的值，最后统计满足条件的 k 的数量即可
# 
# algorithm/codeforce/math/basic/不同周期函数叠加.md 

import init_setting
from cflibs import *
def main(): 
    p, x, y, a = MII()
    
    mods = [1]
    
    for _ in range(p):
        mods.append(mods[-1] * x % p)
        if mods[-1] == 1:
            mods.pop()
            break
    
    k = len(mods)
    pos = [-1] * p
    
    for i in range(k):
        pos[mods[i]] = i
    
    ans = 0
    for i in range(1, p):
        v = pow(i, p - 2, p) * y % p
        if pos[v] >= 0:
            j = pos[v]
            res = ((j - i) * p + i) % (k * p)
            ans += (a - res) // (k * p) + 1
    
    print(ans)