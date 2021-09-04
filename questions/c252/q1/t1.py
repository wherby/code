import math
class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = int(math.sqrt(n))+1
        for i in range(2,m):
            if n//i *i ==n and n//i != i:
                return False
            if n//i* i ==n and n //i ==i:
                return True
        return False

print(Solution().isThree(16))