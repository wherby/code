# https://leetcode.cn/problems/subsequence-after-one-replacement/solutions/3991828/san-zhi-zhen-pythonjavacgo-by-endlessche-2qdj/


class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        dp = [0]*2 
        n = len(s)
        for a in t :
            if a == s[dp[1]]:
                dp[1] +=1 
            dp[1] = max(dp[1],dp[0]+1)
            if a == s[dp[0]]:
                dp[0] +=1
            if max(dp) == n :
                return True 
        return False