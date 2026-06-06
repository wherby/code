# https://codeforces.com/gym/104782/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0601/solution/cf104782i.md
# 题目的队列是一个T长度的周期函数，由于K可能不满足整除T，所以可以看做两个周期，所以可以分为两个组合数相乘



import init_setting
from cflibs import *
from lib.combineWithPreCompute import *
def main():
    M = 5 * 10 ** 6 + 5
    mod = 10 ** 9 + 7
    
    f = Factorial(M, mod)
    
    k, s, t = MII()
    x, y = divmod(k, t)
    
    ans = 0
        
    for i in range(s + 1):
        if (s - x * i) % (x + 1) == 0:
            j = (s - x * i) // (x + 1)
            
            ans += f.combi(i - 1, t - y - 1) * f.combi(j - 1, y - 1)
            ans %= mod
    
    print(ans)

main()