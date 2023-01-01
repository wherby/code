from math import sqrt

class Solution:
    ## Will timeOUt
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
        
        
so = Solution()
primes= so.primesUpTo(100000)
re = so.getPrimeFactors(1000,primes)
print(re,len(primes))