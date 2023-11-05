class Solution:
    def numberOfUniqueGoodSubsequences(self, b) :
        mod = 10**9 + 7
        dp = [0, 0]
        for c in b:
            dp[int(c)] = (sum(dp) + int(c)) % mod
            print(dp)
        return (sum(dp) + ('0' in b)) % mod
        

binary = "000"
re = Solution().numberOfUniqueGoodSubsequences(binary)
print(re)


# 940 question
# dp[i]: the number of unique subsequence from s[1:i]
# [X X X X X X] a
# 1. do not use s[i]: dp[i] += dp[i-1]
# X X X X a
# X X X X
# X X X X
# X X

# 2. use s[i]         dp[i] += dp[i-1]
# X X X X X a
# X X X X a
# X X X X a
# X X a

# j = s[i] ==0? last0: last1
# dp[i] = dp[i-1]*2 - dp[j-1]

# for(int i  = m +1; i<=n;i++){
#  int j = s[i] ==0? last0[i] : last1[i];
#  dp[i] = dp[i-1]*2 -dp[j-1]
# }

# 0 0 0 0 0 0 0 1 X X X X
#             m
# dp[1]-dp[m] =0
# dp[m+1] =1
# dp[j] = dp[i-1]*2 - dp[j-1]



#if(s[i] =='0'){
#  dp[i][0] = dp[i-1][0] + dp[i-1][1];   //dp[i][0] 记录了多少个以0结尾的个数
# }else{
#  dp[i][1] = dp[i-1][0] + dp[i-1][1] + 1 ; //dp[i][1] 记录了多少个以1结尾的个数
# }