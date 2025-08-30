# https://codeforces.com/problemset/problem/1948/D
# 状态dp[i][j] 是由dp[i+1][j+1] 转移而来，但是对于dp[i][j] 有值的时候，并不保证是从对应一个正确的状态
# 只有确定i,j之间的字符串都能被匹配，dp[i][j]才是正确的状态

def testLcp(s):
    n = len(s)
    dp= [[0]* (n+1) for _ in range(n+1)]
    mx = 0
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i] == s[j] or s[i] == "?" or s[j] == "?":
                dp[i][j] = dp[i+1][j+1] +1 
            else:
                dp[i][j]  = 0 
            if dp[i][j] >= j-i:
                mx = max(mx,j-i)
    return 2*mx

input = ["zaabaabz",
"?????",
"code?????s",
"codeforces"
]
for a in input:
    print(testLcp(a))
