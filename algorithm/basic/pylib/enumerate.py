
st ="abcad"

for i,a in enumerate(st):
    print(i,a)


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        print(s)
        if len(s)<2:return '' 
        for i,val in enumerate(s):
            if (val.islower() and val.upper() not in s) or (val.isupper() and val.lower() not in s) :
                return max(self.longestNiceSubstring(s[:i]),self.longestNiceSubstring(s[i+1:]),key=len)
        return s

re = Solution().longestNiceSubstring(st)