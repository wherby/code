from math import sqrt

class Solution:
    def primesUpTo(self, n):
        visited=[0]*(n+2)
        res =[]
        for i in range(2,n+1):
            if visited[i]: continue
            res.append(i)
            for j in range(i,n+1,i):
                visited[j] =1
        return set(res)

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
primes= so.primesUpTo(10000)
re = so.getPrimeFactors(1000,primes)
print(re,len(primes))