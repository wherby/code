# https://codeforces.com/gym/106601/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0624/solution/cf106601l.md
# 这里如果是多位数，就简化为nim问题
# 但是B可能很大，所以需要使用分块讨论的方式，把问题变成小于等于2位，和大于2位的区间
# 对于两位的区间，讨论B的大小会有无限的范围，直接讨论余数的可能值。因为 r+ B*r = x  r<B , r*(B+1)=x 所以有 i*(i+2) > x 的时候，余数就不满足的条件


import init_setting
from cflibs import *
def main():
    x = II()
    ans = 0
    
    for i in range(2, 10 ** 6 + 5):
        cnt = 0
        xor_val = 0
        cur = x
        
        while cur:
            cnt += 1
            xor_val ^= cur % i
            cur //= i
        
        if cnt <= 2: break
        
        if xor_val == 0:
            ans += 1
    
    for i in range(1, 10 ** 6 + 5):
        if i * (i + 2) > x: break
        if x % i == 0:
            ans += 1
    
    print(ans)