# https://codeforces.com/gym/106259/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0509/solution/cf106259b.md
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0509/personal_submission/cf106259b_yawn_sean.py
# 计算排列[x1,x2..xn], f(1) = x1 ,f(j) = f(j-1)//x[j] 
# 观察得到 如果f(j)不为0 的时候，排列中x2..xn的不是1 的个数不能大于20个
# 所以用排列计算所有不等于1的个数的组合数中 x2*x3..*xn  的乘积对应的组合数量，使用DP计算
# 而整除计算可以用组合算法，用乘积先得到，然后再除，algorithm/codeforce/docs/basic/整除传递特性.md
# 然后用前缀和计算方法，得到每个整除值的组合的个数



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    mod = 998244353
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        cnt = [0] * (n + 1)
        for x in nums:
            cnt[x] += 1
        
        res = [0] * (n + 1)
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        comb_val = 1
        
        for i in range(fmin(k, 20)):
            val = pow(cnt[1], k - 1 - i, mod) * comb_val % mod
            
            for j in range(n + 1):
                if dp[j]:
                    res[j] = (res[j] + dp[j] * val) % mod
            
            flg = True
            ndp = [0] * (n + 1)
            for j in range(1, n + 1):
                if dp[j]:
                    for w in range(2, n // j + 1):
                        if cnt[w]:
                            flg = False
                            ndp[j * w] = (ndp[j * w] + dp[j] * cnt[w] % mod) % mod
            
            if flg: break
            
            dp = ndp
            comb_val = comb_val * (k - 1 - i) % mod * pow(i + 1, -1, mod) % mod
        
        acc = cnt[:]
        for i in range(n):
            acc[i + 1] += acc[i]
    
        ans = 0
        for i in range(1, n + 1):
            for j in range(i - 1, n + 1, i):
                ans = (ans + (acc[fmin(j + i, n)] - acc[j]) * (j // i + 1) % mod * res[i] % mod) % mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))