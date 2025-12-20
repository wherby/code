# https://codeforces.com/gym/105874/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1216/solution/cf105874g.md
# 针对K取值的大小， 使用平方根特性， 对小数字递推，对大的数字使用排列组合特性计算
# 处理DP 和 prefix sum 对于同一个k 分别计算


import init_setting
from cflibs import *
from lib.combineWithPreCompute import *

def main(): 
    M = 2 * 10 ** 5
    mod = 998244353
    
    f = Factorial(M * 2, mod)
    
    saved_dp = [[0] * (M + 1) for _ in range(451)]
    #print("st")
    for i in range(1, 451):
        #print(i)
        saved_dp[i][0] = 1
        
        for j in range(1, M + 1):
            saved_dp[i][j] = saved_dp[i][j - 1]
            if j >= i:
                saved_dp[i][j] += saved_dp[i][j - i]
            saved_dp[i][j] %= mod
        
        for j in range(1, M + 1):
            saved_dp[i][j] += saved_dp[i][j - 1]
            saved_dp[i][j] %= mod
    #print("i")
    n, q = MII()
    outs = []
    
    for _ in range(q):
        l, r, k = MII()
        if k <= 450:
            outs.append((saved_dp[k][r] - saved_dp[k][l - 1]) % mod)
        else:
            ans = 0
            
            for cnt_k in range(r // k + 1):
                lbound = fmax(l - cnt_k * k, 0) - 1
                rbound = r - cnt_k * k
                
                ans += f.combi(rbound + cnt_k + 1, cnt_k + 1) - f.combi(lbound + cnt_k + 1, cnt_k + 1)
                ans %= mod
            
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))

main()