class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        d = [0]*(n+1)
        d[n] =0
        d[n-1]=1
        for i in range(n-2,-1,-1):
            d[i] =1 
            for j in range(i+1,n,1):
                leng = j -i 
                if j + leng > n :
                    break
                if s[i:j] ==s[j:j+leng]:
                    d[i] = max(d[i],d[j] +1)
        return d[0]