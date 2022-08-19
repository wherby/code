class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [0]*26
        for a in s:
            t = ord(a) - ord('a')
            for j in range(max(0,t-k),min(26,t+k+1)):
                dp[t] = max(dp[j]  ,dp[t])
            dp[t] +=1
            #print(dp)
        return max(dp)
        


re =Solution().longestIdealString("azaza",25)
print(re)