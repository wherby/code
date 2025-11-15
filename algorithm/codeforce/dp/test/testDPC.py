# https://codeforces.com/gym/106188/problem/G

def findC(ls,k):
    ls.sort()
    M = max(ls)*k
    dp = [[0]*(M+1) for _ in range(k+1)]
    dp[0][0] =1
    for a in ls:
        for k1 in range(k,0,-1):
            for j in range(M,a-1,-1):
                if k1 == k :
                    if a <j-a:
                        dp[k1][j] += dp[k1-1][j-a]
                else:
                    dp[k1][j] += dp[k1-1][j-a]
    return sum(dp[k])
    

ls = [1,2,3,3,3]
ls = [1,5,2,3,4,1]
print(findC(ls,4))