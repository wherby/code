class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def valid(s):
            n = len(s)
            for i in range(n/2):
                if s[i] != s[n-1-i]:
                    return False
            return True

        n = len(s)
        for i in range(n/2):
            if s[i] != s[n-1-i]:
                s1 =s[:i] + s[i+1:]
                s2 = s[:n-1-i] + s[n-i:]
                if valid(s1) == False and valid(s2) == False:
                    #print s1,s2
                    return False
                else:
                    return True
        return True

s=Solution()
print s.validPalindrome("aba")
print s.validPalindrome("abcda") 