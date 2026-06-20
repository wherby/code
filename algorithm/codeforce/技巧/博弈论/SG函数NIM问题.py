# https://codeforces.com/gym/104668/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0619/solution/cf104668l.md


import init_setting
from cflibs import *

def main():
    n, a, b = MII()
    nums = LII()
    
    ma1 = 0
    ma2 = 0
    
    for x in nums:
        if x > ma1:
            ma1, ma2 = x, ma1
        elif x > ma2:
            ma2 = x
    
    if a == b:
        val = 0
        for x in nums:
            val ^= x % (a + 1)
        print('Petyr' if val else 'Varys')
    
    elif a > b:
        if ma1 > b: print('Petyr')
        else:
            val = 0
            for x in nums:
                val ^= x % (b + 1)
            print('Petyr' if val else 'Varys')
    
    else:
        if ma2 > a: print('Varys')
        else:
            val = 0
            for x in nums:
                val ^= x % (a + 1)
            
            if ma1 <= a:
                print('Petyr' if val else 'Varys')
            else:
                target = (ma1 % (a + 1)) ^ val
                print('Petyr' if target <= a and ma1 - target <= a else 'Varys')