import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = int(math.sqrt(num))
        sm = 0
        for i in range(2,n+1):
            if num%i ==0:
                sm +=i 
                sm += num //i
        return sm +1 == num

re = Solution().checkPerfectNumber(28)
print(re)

