# https://codeforces.com/gym/101192/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0929/solution/cf101192a.md
# 求GCD的子数组数，采用了容斥原理
# 这里GCD需要满足LIS 特性，对每个备选项的时候，需要递增，此时由于值域分散，所以在值域重排后计算
# 这里其实是在LIS的排序下进行GCD子数组的枚举



import init_setting
from cflibs import *
def main():
    M = 10 ** 6 + 5
    pr = list(range(M))
    
    for i in range(2, M):
        if pr[i] == i:
            for j in range(i, M, i):
                pr[j] = i
    
    n = II()
    mod = 10 ** 9 + 7
    
    v1 = LII()
    v2 = LII()
    
    def factors(x):
        ans = [1]
        while x > 1:
            p = pr[x]
            c = 0
            while x % p == 0:
                x //= p
                c += 1
            
            for i in range(c * len(ans)):
                ans.append(ans[i] * p)
        
        return ans
    
    pos = [[] for _ in range(M)]
    
    for i in range(n):
        for x in factors(v2[i]):
            pos[x].append(i)
    
    del pr
    
    sorted_v1 = sorted(v1)
    v1 = [bisect.bisect_left(sorted_v1, x) for x in v1]
    
    del sorted_v1
    
    cnt = [0] * M
    tmp = [0] * n
    
    fen = FenwickTree(n)
    
    for i in range(M):
        for j in pos[i]:
            tmp[j] = (fen.rsum(0, v1[j] - 1) + 1) % mod
            cnt[i] = (cnt[i] + tmp[j]) % mod
            fen.add(v1[j], tmp[j])
        
        for j in pos[i]:
            fen.add(v1[j], -tmp[j])
    
    for i in range(M - 1, 0, -1):
        for j in range(2 * i, M, i):
            cnt[i] -= cnt[j]
            cnt[i] %= mod
    
    print(sum(i * cnt[i] % mod for i in range(M)) % mod)