# https://codeforces.com/gym/103306/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0715/solution/cf103306k.md
# 利用倍数容斥的原理，使用莫比乌斯函数计算
# k*d= n d是循环节的长度，k是循环节的倍数，这里是对循环节的倍数求莫比乌斯函数变成求和系数


import init_setting
from cflibs import *
def main():
    M = 10 ** 6 + 5
    mod = 10 ** 9 + 7
    
    pr = list(range(M))
    phi = [1] * M
    
    phi[0] = 0
    
    for i in range(2, M):
        if pr[i] == i:
            for j in range(i, M, i):
                pr[j] = i
                if j % (i * i) == 0:
                    phi[j] = 0
                else:
                    phi[j] = -phi[j]
    
    cur = 1
    ans = [0] * M
    
    for i in range(1, M):
        cur = cur * 2 % mod
        
        for j in range(2 * i, M, i):
            ans[j] += (-phi[j // i]) * cur % mod
            ans[j] %= mod
    
    t = II()
    outs = []
    
    for _ in range(t):
        outs.append(ans[II()])
    
    print('\n'.join(map(str, outs)))