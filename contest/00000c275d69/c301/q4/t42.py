from functools import cache
class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        sm = 0
        mem ={}
        @cache
        def getMem(n,mx):
            if n ==0:
                return 1
            ret =0
            for i in range(1,mx+1):
                ret += getMem(n-1,mx//i)
                #print(getMem(n-1,mx//i),n-1,mx//i,ret)
            return ret 
        sm=getMem(n,maxValue)
        #print(mem)
        mod = 10**9+7
        return sm %mod


#re =Solution().idealArrays(n = 5878, maxValue = 2900)
re =Solution().idealArrays(n = 37, maxValue = 71)
#re = Solution().idealArrays(n = 2, maxValue = 5)
print(re)