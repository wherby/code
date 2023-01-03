from math import sqrt

class PrimeOfNumber:
    ## set the prime to n
    def __init__(self,n) -> None:
        primes = set(range(2, n + 1))
        for i in range(2, n):
            if i in primes:
                it = i * 2
                while it <= n:
                    if it in primes:
                        primes.remove(it)
                    it += i
        self.primes = primes
        
    def getPrimeFactors(self, n):
        ret = {}
        sq = int(sqrt(n)) # could use to accelarate the prime selection

        for p in self.primes:
            if n in self.primes:
                ret[n] = 1
                break

            while n % p == 0:
                ret[p] = ret.get(p, 0) + 1
                n //= p

            if n <= 1:
                break

        return ret

pls = PrimeOfNumber(10**5)
#print(pls.primes)
print(pls.getPrimeFactors(16000))