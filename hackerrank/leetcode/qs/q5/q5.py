# Longest Palindromic Substring

#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#https://leetcode.com/problems/longest-palindromic-substring/description/



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        mx = []
        re1 =[]
        re2 =[]
        for i in range(n):
            mx.append([0]*n)
            re1.append(i)
        mxLen = 1
        mxLenIndex = 0

        for i in range(n):
            mx[0][i] =1
            if i +1 <n:
                if s[i] == s[i+1]:
                    mx[1][i]=1
                    mxLenIndex = i
                    mxLen =2
                    re2.append(i)
        for i in range(2,n):
            tre =[]
            if i%2 ==0:
                re = re1
            else:
                re = re2

            for j in re:
                if j-i/2 >=0 and j+i-i/2<n:
                    if s[j - i/2] ==s[j +i -i/2] and mx[i-2][j] ==1:
                        mx[i][j] =1
                        mxLen = i+1
                        mxLenIndex = j
                        tre.append(j)
            if i %2 == 0:
                re1 =tre
            else:
                re2 = tre
        return s[mxLenIndex-(mxLen-1)/2: mxLenIndex+mxLen-(mxLen-1)/2 ]




s = Solution()
str1 = "bananas"
print s.longestPalindrome(str1)