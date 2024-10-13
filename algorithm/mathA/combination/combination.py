# Get combination of C(m,n) https://www.youtube.com/watch?v=FxGWaG9danM  
# will stack overflow
#   [Previous line repeated 699 more times]
#   File "c:\Users\where\Documents\github\code\algorithm\mathA\combination.py", line 8, in getComb
#     if self.comb[m][n] !=0:
# IndexError: list index out of range
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


comb = Comb(10000,1000)
re = comb.getComb(100,400)
print(re)
#print(comb) 
