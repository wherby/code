class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo=hi=0

        for c in s:
            lo = lo+1 if c =='(' else  lo-1
            hi += 1 if c !=')' else  -1
            if hi <0:
                break
            lo = max(0,lo)
        print lo
        return lo ==0

s =Solution()
print s.checkValidString("(*)")