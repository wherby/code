
# https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/?envType=daily-question&envId=2026-03-07
# 使用奇偶性的特点，不用分别讨论

class Solution:
    def minFlips(self, s: str) -> int:
        ans = n = len(s)
        acc = 0 
        for i in range(2*n):
            acc += (ord(s[i%n]) +i)%2 
            left = i-n+1
            if left <0:
                continue
            ans =min(ans,acc,n-acc)
            acc -=(ord(s[i%n]) +i)%2 
        return ans