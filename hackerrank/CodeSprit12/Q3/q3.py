import math

def getPrimes(n,pl):
    isPrime =True
    for i in range(2,int(math.sqrt(1+n))+1):
        if n%i ==0 :
            pl.append(i)
            n=n/i
            isPrime = False
            getPrimes(n,pl) 
            break
    if isPrime == True:
        pl.append(n)
    return pl


def getNumber(n,k,sm):
    primeLs = getPrimes(n,[])
    primeLs = set(primeLs)
    primeLs = sorted(primeLs)
    primeLs =primeLs[::-1]
    if n ==1:
        return sm +k
    for i in primeLs:
        if n%i ==0 and n!= i:
            sm = sm + k
            k = k*i
            n = n/i
            return getNumber(n,k,sm)
        if n == i:
            sm = sm +k
            k = k *i
            n =1
            getNumber(1,k,sm)
    return getNumber(1,k,sm)
     


def getPrimeLs(n):
    ls = range(2,int((n+1) **0.5))
    pls = filter(isPrime,ls)
    print pls
    return pls

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

primeLs=getPrimeLs(1000000)
primeLs = primeLs[::-1]
print getNumber(36,1,0)
print getPrimes(100,[])