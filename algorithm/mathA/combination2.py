# Get combination of C(m,n) https://www.youtube.com/watch?v=FxGWaG9danM  
import sys
sys.setrecursionlimit(1500000)
class Comb():
    def __init__(self,m,n) -> None:
        self.comb =[[0]*(n+1) for i in range(m+1)]
        self.mod = 10**9+7

    def getComb(self,m,n):
        if self.comb[m][n] !=0:
            return self.comb[m][n]
        if n > m-n:
            return self.getComb(m,m-n)
        if n ==0: return 1
        if n==1: return m
        a = self.getComb(m-1,n-1)
        b =self.getComb(m-1,n)
        self.comb[m][n] = (a+b) %self.mod
        return self.comb[m][n]


comb = Comb(1000,1000)
for i in range(1000):
    for j in range(i):
        comb.getComb(i,j)
#print(comb.comb)
re = comb.getComb(1000,400)
print(re)
#print(comb) 
