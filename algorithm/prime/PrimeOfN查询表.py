

M = 2 * 10 ** 5
pr = list(range(M + 1))

for i in range(2, M + 1):
    if pr[i] == i:
        for j in range(i, M + 1, i):
            pr[j] = i


def getPrime(x):
    prs = []
    cur = x 
    while cur >1:
        p = pr[cur]
        while cur % p == 0 :
            prs.append(p)
            cur //=p 
    return prs 

print(getPrime(10024))
print(getPrime(11000))