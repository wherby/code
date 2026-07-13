# https://codeforces.com/gym/106054/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0709/solution/cf106054m.md
# 对非简单路径的冗余路径计算，利用了冗余路径的单向递推特性，寻找到向量点的下一个冗余值的路径次数
# 这里因为每天的限制是k步，所以这里使用了反射原理减去非法的分布 algorithm/mathA/combination/卡特兰数反射原理/卡特兰数反射原理.md
# 而在选择非法的分布的天数时候，引入了二项式系数，所以这里使用二项式反演计算 algorithm/mathA/combination/docs/二进制反演和对偶拆分等式.md
# 所以在反射的时候，因为计算分配超过k的天数之后与分配剩余的数量的分布下，在叠加剩余分配的时候，有可能当前的分配超过了预先cnt天的假设，所以这种情况需要二进制容斥？ 
# 但是这里计算分布次数的时候直接使用 空余步数法（对偶拆分）的话更简单 algorithm/mathA/combination/docs/二进制反演和对偶拆分等式.md



import init_setting
from cflibs import *
from lib.combineWithPreCompute import * 
def main():
    n, m, k = MII()
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    dis = [-1] * n
    dis[0] = 0
    
    que = [0]
    
    for u in que:
        for v in path[u]:
            if dis[v] == -1:
                dis[v] = dis[u] + 1
                que.append(v)
    
    if dis[1] == -1:
        print(0)
        exit()
    
    mod = 998244353
    f = Factorial(10000, mod)
    
    dp = [[0] * n for _ in range(k)]
    
    dp[0][0] = 1
    
    for i in range(k):
        for u in que:
            if dp[i][u] == 0:
                continue
            
            for v in path[u]:
                ni = dis[u] + i + 1 - dis[v]
                if ni < k:
                    dp[ni][v] += dp[i][u]
                    dp[ni][v] %= mod
    
    ans = 0
    days = (dis[1] - 1) // k + 1
    
    for i in range(k):
        if dis[1] + i <= days * k:
            res = 0
            
            for cnt in range(days + 1):
                resid = dis[1] + i - cnt * k
                if cnt % 2 == 0:
                    res += f.combi(resid - 1, days - 1) * f.combi(days, cnt) % mod
                else:
                    res += mod - f.combi(resid - 1, days - 1) * f.combi(days, cnt) % mod
                res %= mod
            
            ans += res * dp[i][1] % mod
            ans %= mod
    
    print(ans)