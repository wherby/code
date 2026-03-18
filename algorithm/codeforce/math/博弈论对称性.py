# https://codeforces.com/gym/106407/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0309/solution/cf106407a.md
# 对于双偶数的情况，在k =2 或者3，k==3 时候后手一定能凑成4的倍数，前手无法凑成4的倍数，所以后手获胜，在k==2时候，后手就中心对称就可以了。
# 对于k=1的情况，则与奇偶性相关
# 对于其他情况，先手一定可以找到中心点，然后对称操作

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, k = MII()
        
        if k == 1: outs.append('Munir' if n * m % 2 else 'Matthew')
        elif n % 2 or m % 2 or k >= 4: outs.append('Munir')
        else: outs.append('Matthew')
    
    print('\n'.join(outs))