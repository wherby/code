
from math import sqrt


def primeUpTo(n):
    primes = set(range(2,n+1))
    for i in range(2,n):
        if i in primes:
            it = i*2
            while it <=n:
                if it in primes:
                    primes.remove(it)
                it +=i 
    return primes

def getPrimeForFactots(n,primes):
    ret ={}
    for p in primes:
        if n  in primes:
            ret[n] =1 
            break
        
        while n % p ==0:
            ret[p] = ret.get(p,0) +1
            n //=p 
        if n <=1:
            break
    return ret

ps = primeUpTo(10**4)
print(getPrimeForFactots(720,ps))
ls = getPrimeForFactots(720,ps)
for a in ls:
    print(a,ls[a])