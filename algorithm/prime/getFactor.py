
def getPrime(n):
    ret = [i for i in range(n+1)]
    for i in range(2,n+1):
        if ret[i] == i:
            for j in range(i*2,n+1,i):
                ret[j] = i
    return ret 
pms = getPrime(10**6+2)

def getFactor(n):
    ret =[]
    cur = n
    while cur !=1:
        b= pms[cur]
        ret.append(b)
        while cur %b ==0:
            cur = cur //b 
    return ret 

print(getFactor(1029))