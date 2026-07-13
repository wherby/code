# https://codeforces.com/gym/103821/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0708/solution/cf103821j.md
# algorithm/codeforce/数论/二项式反演/二项式反演容易错误.md
# 在k个盒子里 计算 恰好等于i个盒子的情况，要注意计算小于等于i个盒子的组合数字的时候，需要先计算选择i个盒子的二项式comb(k,i)作为系数
# 二项式系数导致了不能直接使用简单容斥计算，需要使用二项式容斥计算所有情况
# f(i) = g(i) - g(i-1) g(i) 表示分布在最多i个盒子的组合数，这只有齐次的时候才能这样计算，否则需要二项式反演计算


import init_setting
from cflibs import *
from lib.combineWithPreCompute import * 
def main():
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    f = Factorial(2000, mod)
    
    for _ in range(t):
        n, k = MII()
        cols = LII()
        
        cnt = [0] * (n + 1)
        for c in cols:
            cnt[c] += 1
        
        ans = 0
        
        for i in range(1, k + 1):
            res = f.combi(k, i)
            for v in cnt:
                res = res * f.combi(v + i - 1, i - 1) % mod
            
            if (k - i) % 2: ans -= res
            else: ans += res
    
        ans %= mod
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))