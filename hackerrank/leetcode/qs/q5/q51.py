# Time out for uncessory search
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        mx = []
        for i in range(n):
            mx.append([0]*n)
        mxLen = 1
        mxLenIndex = 0
        for i in range(n):
            mx[0][i] =1
            if i +1 <n:
                if s[i] == s[i+1]:
                    mx[1][i]=1
                    mxLenIndex = i
                    mxLen =2
        for i in range(2,n):
            for j in range(1,n-1):
                if j-i/2 >=0 and j+i-i/2<n:
                    if s[j - i/2] ==s[j +i -i/2] and mx[i-2][j] ==1:
                        mx[i][j] =1
                        mxLen = i+1
                        mxLenIndex = j
        #print mxLenIndex-(mxLen-1)/2, mxLenIndex+mxLen-(mxLen-1)/2
        return s[mxLenIndex-(mxLen-1)/2: mxLenIndex+mxLen-(mxLen-1)/2 ]

s = Solution()
str1 = "abcba"
print s.longestPalindrome(str1)