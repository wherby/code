# https://codeforces.com/gym/105973/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1104/solution/cf105973c.md

# n =5
# f(1) =C(1,1),c(2,1),C(3,1),C(4,1),C(5,1)
# f(2)=        C(2,2),C(3,2),C(4,2),C(5,2)
# f(3)=               C(3,3),C(4,3),C(5,3)
# f(4) =                     C(4,4),C(5,4)
# f(5) =                            C(5,5)


import init_setting
from lib.cflibs import *
from lib.combineWithPreCompute import *
def main(): 
    mod = 998244353
    
    M = 10 ** 6
    f = Factorial(M, mod)
    
    acc = [0] * (M + 1)
    for i in range(1, M + 1):
        acc[i] = acc[i - 1] ^ 1 ^ (0 if i % 2 else f.comb(i, i // 2))
    
    t = II()
    outs = []
    
    for _ in range(t):
        outs.append(acc[II()])
    
    print('\n'.join(map(str, outs)))

main()