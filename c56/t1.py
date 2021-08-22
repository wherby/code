import math
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0 
        for i in range(1,n):
            for j in range(i,n):
                t = i*i + j *j
                x= math.sqrt(t)
                if x == int(x) and x <= n :
                    num = num +1
        return num *2

        

a =Solution().countTriples(250)
print(a)