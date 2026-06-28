# https://codeforces.com/gym/106601/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0624/solution/cf106601k.md
M = 10**5

pr =list(range(M+1))

for i in range(2,M+1):
    if pr[i] == i:
        for j in range(i,M+1,i):
            pr[j] = i 

def factors(x):
    if x ==0:return [] 
    res = [1]
    
    while x >1:
        p = pr[x]
        c = 0
        while x %p ==0:
            x //= p 
            c +=1
        l = len(res)
        for _ in range(c*l):
            res.append(res[-l]*p)
    return res 

print(factors(999))
print(factors(512))
print(factors(10000))
            