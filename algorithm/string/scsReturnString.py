def superSeqString(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # Below steps follow above recurrence
            if (not i):
                dp[i][j] = j
            elif (not j):
                dp[i][j] = i
 
            elif (X[i - 1] == Y[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
 
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1])
    N = dp[m][n]
    re = ""
    idxX = m-1
    idxY = n-1
    for _ in range(N):
        if X[idxX] == Y[idxY]:
            re +=X[idxX]
            idxX ,idxY = idxX-1,idxY -1
        elif dp[idxX][idxY+1]+1 == dp[idxX+1][idxY+1]:
            re += X[idxX]
            idxX -=1
        else:
            re +=Y[idxY]
            idxY -=1
    return re[::-1]

#  [[0, 1, 2, 3, 4, 5, 6, 7],
#   [1, 2, 3, 4, 5, 5, 6, 7], 
#   [2, 2, 3, 4, 5, 6, 7, 8], 
#   [3, 3, 4, 5, 6, 7, 8, 9], 
#   [4, 4, 5, 5, 6, 7, 8, 9], 
#   [5, 5, 6, 6, 7, 7, 8, 9],
#   [6, 6, 7, 7, 8, 8, 9, 9]]
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
re =superSeqString(X, Y)
print(re)