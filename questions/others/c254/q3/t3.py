from collections import defaultdict
class Solution:
    def conntV(self,p):
        CONSTV =10**9 +7
        t =p
        acc =2**p -2
        res = 2**p -2
        while t > 0:
            res =res *res % CONSTV
            acc = acc + res  % CONSTV
        return res
    def minNonZeroProduct(self,p ) :
        # self.dic = defaultdict(int)
        # n =31
        # while n >0:
        #     self.countZero(n)
        #     n-=1
        #print(self.dic)
        if p ==1:
            return 1
        if p ==2:
            return 6
        n = 2**(p-1)-1
        t = 2**p
        CONSTV =10**9 +7
        t2 =t-2
        res =1
        while n >0:
            if n %2 ==1:
                res *= t2
            t2 = t2*t2%CONSTV
            n=n//2
        res = res *(t-1)%CONSTV
        return res

a=Solution().minNonZeroProduct(3)
print(a)