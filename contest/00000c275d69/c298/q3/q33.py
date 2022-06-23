class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [k + 1] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] > k:
                    continue
                if dp[j] * 2 + int(s[i]) <= k:
                    dp[j + 1] = min(dp[j + 1], dp[j] * 2 + int(s[i]))
        print(dp)
        for i in range(n, -1, -1):
            if dp[i] <= k:
                return i
            
        return -1
    
re =Solution().longestSubsequence(s = "00101111110000", k =1)
print(re)