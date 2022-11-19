# https://leetcode.com/contest/weekly-contest-319/problems/maximum-number-of-non-overlapping-palindrome-substrings/
## https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/2809233/python-dp-solution/

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(k - 1, n):
            dp[i] = dp[i - 1]
            if dp[i] <= dp[i-k] and s[i-k+1:i+1] == s[i-k+1:i+1][::-1]:
                dp[i] = dp[i - k] + 1
            elif i - k >= 0 and dp[i] <= dp[i-k-1] and s[i-k:i+1] == s[i-k:i+1][::-1]:
                dp[i] = dp[i - k - 1] + 1
        return dp[n - 1]
    
re =Solution().maxPalindromes(s = "iqqibcecvrbxxj",k=3)
print(re)