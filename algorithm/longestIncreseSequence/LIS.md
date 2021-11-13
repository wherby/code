# Longest increase sequece O(nlogn)

        sk =[]
        for x in ls:
            if len(sk) == 0 or x > sk[-1]:
                sk.append(x)
            else:
                idx = bisect_left(sk,x)  #use bisect_right may out of index when same value
                sk[idx] = x
            

# Longest common sequece O(n^2)

if s[i] == s[j]:
    dp[i][j] = dp[i-1][j-1]+1
else:
    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# if one of compare string is unique char , then LCS can be change to LIS
questions/c222/q4.py
https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/
https://www.youtube.com/watch?v=2cYsXuYYWmk
