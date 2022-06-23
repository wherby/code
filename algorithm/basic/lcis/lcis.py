def lcis(a,b):
    m,n = len(a),len(b)
    dp = [[0 for _ in range(n+1) ] for _ in range(m+1)]
    a=[0]+a
    b = [0]+b
    for i in range(1,m+1):
        curVal = 0
        if b[0] < a[i]: #??
            curVal = dp[i-1][0]
        for j in range(1,n+1):
            if a[i] == b[j]:
                dp[i][j] = curVal +1
            else:
                dp[i][j] = dp[i-1][j]
            if b[j] < a[i]:
                curVal = max(curVal, dp[i-1][j])
    #print(dp)
    return dp[m][n]

a = [1,4,2,3,6,7,4,5,6]
b = [1,2,4,5,6]
re=lcis(a,b)
print(re)