class Solution:
    def appealSum(self, s: str) -> int:
        c=[0]*26
        cnt = 0
        for i,a in enumerate(s):
            k = ord(a)-ord('a')
            c[k] = i+1
            for j in range(26):
                cnt += c[j]
        return cnt

re =Solution().appealSum("code")
print(re)