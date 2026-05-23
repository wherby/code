# https://codeforces.com/gym/106052/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0514/solution/cf106052c.md
# 题目求 1<=x,y<=n 的条件下，max(x,y)/gcd(x,y) 是奇数的组合数目

# 在数论中求 max(x,y)/gcd(x,y) 是奇数的数目不好计算，但是 x=x1*a ,y = y1 *a 则变形为 max(x1,y1)是奇数 且 gcd(x1,y1) =1 
# gcd(x1,y1) =1 的个数就等于phi函数，变形为求奇数的phi函数
# 由于考虑了GCD因子，所以需要再区间内找到可能的倍数为奇数的欧拉数
# $$W = \sum_{g=1}^{n} \sum_{m=3, 5, \dots}^{\lfloor n/g \rfloor} 2\phi(m)$$
# 所以对这个累加变形，把phi 函数变成 phi 前缀和， i就表示了当gcd值为 i 的时候，求出的n的奇数phi值前缀和




import init_setting
from cflibs import *
def main():  
    M = 10 ** 6 + 5
    phi = list(range(M))
    
    for i in range(2, M):
        if phi[i] == i:
            for j in range(i, M, i):
                phi[j] = phi[j] // i * (i - 1)
    
    for i in range(2, M):
        if i % 2 == 0:
            phi[i] = 0
        else:
            phi[i] = 2 * phi[i]
    
    for i in range(1, M):
        phi[i] += phi[i - 1]
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        ans = 0
        
        for i in range(1, n + 1):
            ans += phi[n // i]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))