# DP里保存的值是 从最高位到当前位置，没有受到上届约束的所有数字有i个1的时候的个数，c保持的是到当前位置的时候，上届有多少个1


def countToM(m):
    m = m+1
    dp = [0]*60
    c = 0 
    
    for i in range(59,-1,-1):
        for j in range(58,-1,-1):
            dp[j+1] += dp[j]
        if m >>i &1 :
            dp[c] +=1
            c +=1
    return dp 
print(countToM(10**8))