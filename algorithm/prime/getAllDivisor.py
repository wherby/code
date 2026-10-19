# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0929/solution/cf101192a.md

M = 10**5+5
pr = list(range(M))

for i in range(2,M):
    if pr[i] == i:
        for j in range(i,M,i):
            pr[j] = i 

def factors(x):
    ans =[1]
    while x>1:
        p = pr[x]
        c = 0
        while x%p ==0:
            x //=p 
            c +=1
        for i in range(c*len(ans)):
            ans.append(ans[i] * p )
    return ans 

print(factors(1000))