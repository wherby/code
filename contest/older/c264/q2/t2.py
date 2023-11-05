from collections import defaultdict
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def con(n):
            ls =[0]*11
            while n >0:
                t = n %10
                ls[t] +=1
                n =n //10
            print(n,ls)
            for i in range(1,10):
                if (ls[i] != i and ls[i] != 0) or ls[0] !=0:
                    return False
            return True
        for i in range(n+1,666669):
            if con(i):
                return i


re=Solution().nextBeautifulNumber(1000)
print(re)