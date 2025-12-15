# https://codeforces.com/gym/105284/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1213/solution/cf105284c.md
# 本题化简为两个独立期望的计算量，理论存在的点数量， 和理论存在的边数量的差值
# 边的期望是 1/(i+1)*i [1,N-1] 上的求和， 裂项边成 1/i - 1/(i+1)，裂项求和的到 1-1/N



import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    M = 10 ** 6
    mod = 10 ** 9 + 7
    
    f = Factorial(M, mod)
    
    acc = [0] * (M + 1)
    
    for i in range(1, M + 1):
        acc[i] = (acc[i - 1] + f.inv(i)) % mod
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        outs.append((acc[n] - (1 - f.inv(n))) % mod)
    
    print('\n'.join(map(str, outs)))

main()