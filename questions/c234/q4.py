class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        def nearK(n):
            n3 = n //3
            n = n % 3
            n2=0
            if n ==1 and n3>0:
                n3-=1
                n2=2
            if n ==2:
                n2 =1
            return (n2,n3)
        n2,n3 =nearK(primeFactors)
        mod = 10**9 +7
        def quickPow(x,y):
            ret =1
            cur = x 
            while y >0:
                if y & 1:
                    ret = ret * cur % mod
                cur = cur *cur % mod
                y = y //2
            return ret
        res = quickPow(3,n3)
        r2 =quickPow(2,n2)
        res =res *r2 %mod
        return res
        
            
            




