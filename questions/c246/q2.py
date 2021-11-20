# This code can't pass pyhon2 for div op in python2 is diff from py3
import math
class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        s = startTime.split(":")
        f = finishTime.split(":")
        s1,s2 = int(s[0]),int(s[1])
        f1,f2 = int(f[0]),int(f[1])
        if f1 < s1:
            f1 += 24
        if f1 == s1 and s2 >f2:
            f1 += 24
        res  = (f1-s1)*4 - math.ceil(s2/15) + math.floor(f2/15)
        res = max(res,0)
        return int(res)

startTime = "12:01"
finishTime = "12:44"
re = Solution().numberOfRounds(startTime = "12:01", finishTime = "12:44") 
print(re)