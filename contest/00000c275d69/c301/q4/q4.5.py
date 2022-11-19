from math import sqrt
def comb2(n,m):
    cnt = 1
    for i in range(m):
        cnt *=n-i
        cnt //= i+1
    return cnt
class Solution(object):
    def primesUpTo(self, n):
        primes = set(range(2, n + 1))
        for i in range(2, n):
            if i in primes:
                it = i * 2
                while it <= n:
                    if it in primes:
                        primes.remove(it)
                    it += i

        return primes

    def getPrimeFactors(self, n, primes):
        ret = {}
        sq = int(sqrt(n))

        for p in primes:
            if n in primes:
                ret[n] = 1
                break

            while n % p == 0:
                ret[p] = ret.get(p, 0) + 1
                n //= p

            if n <= 1:
                break

        return ret
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        primes = self.primesUpTo(maxValue)
        sm = 0
        mod = 10**9+7
        for i in range(1,maxValue+1):
            factors = self.getPrimeFactors(i,primes)
            cur =1
            for k in factors:
                ct  =factors[k]
                t = comb2(n+ct-1,ct)
                cur *=t%mod
            sm += cur 
            #print(cur,i)
        return sm%mod
                
re = Solution().idealArrays(n = 2, maxValue = 5)
re = Solution().idealArrays(n = 10000, maxValue = 9999)

print(re) 