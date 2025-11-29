
M= 10**5

def getPrime(M=M):
    is_prime = [1]*(M+1)
    prs =[]
    for i in range(2,M+1):
        if is_prime[i]:
            prs.append(i)
            for j in range(2*i,M+1,i):
                is_prime[j] = 0 
    return prs
prs = getPrime()
def getAllDiv(n):
    vals = {}
    for p in prs:
        if p*p > n:
            break
        if n%p == 0:
            vals[p] = 0 
            while n%p ==0:
                vals[p] +=1
                n=n // p 
    if n >1:
        vals[n] =1
    factors =[1]
    for x in vals:
        c = vals[x]
        k = len(factors)
        for i in range(c*k):
            factors.append(factors[i]*x)
    return factors

if __name__ == '__main__':
    import math
    ls = range(1,10)
    acc = 1 
    for a in ls :
        acc = a *acc 
    #print(acc)
    allDiv = getAllDiv(acc)
    print(len(allDiv))
    import random 
    random.shuffle(allDiv)
    print(allDiv)
    dicPos = {a:i for i,a in enumerate(allDiv)}
    print(dicPos)
    pos = 0 
    for i in range(1,len(allDiv)):
        if dicPos[math.gcd(allDiv[pos],allDiv[i])] != pos:
            #pos = dicPos[math.gcd(allDiv[pos],allDiv[i])] 
            pos = i
    print(pos,allDiv[pos])