# # 如何用 1<ai<=k 的序列构成乘积为x的序列个数

def getSub(K):
    K, mod = K, 998244353
    dp = [[0] * (K + 1) for _ in range(17)]
    
    dp[0][1] = 1
    
    for i in range(16):
        for j in range(K + 1):
            if dp[i][j]:
                for v in range(2 * j, K + 1, j):
                    dp[i + 1][v] += dp[i][j]
                    if dp[i + 1][v] >= mod:
                        dp[i + 1][v] -= mod
    print(dp)

getSub(10)