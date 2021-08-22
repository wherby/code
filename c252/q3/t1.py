import math
class Solution(object):
    def findx(self, needApple):
        sm =0
        for i in range(1000000):
            sm += 12 * i*i
            if sm >=needApple:
                return i

    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        return self.findx(neededApples)*8
        
print(Solution().minimumPerimeter(1))