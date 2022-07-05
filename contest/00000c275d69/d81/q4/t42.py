import math
class Matrix():
    def __init__(self) -> None:
        self.mod = 10**9+7
        
    def mutliply(self, m1,m2):
        n = len(m1)
        ret = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                t =0 
                for k in range(n):
                    t += m1[i][k]*m2[k][j]
                ret[i][j] = t %self.mod
        return ret
    def pow(self, mx,y):
        n = len(mx)
        ret =[[0]*n for _ in range(n)]
        for i in range(n):
            ret[i][i] =1
        cur = mx 
        while y>0:
            if y & 1:
                ret = self.mutliply(ret,cur)
            cur = self.mutliply(cur,cur)
            y = y //2
        return ret
    
    def dot(self,mx,ls):
        m = len(ls)
        ret = [0]*m
        for i in range(m):
            t = 0
            for k in range(m):
                t +=  mx[i][k]*ls[k]
            ret[i] =t
        return ret 
                
class Solution:
    def distinctSequences(self, n: int) -> int:
        Sx = [0]*36

        mxp = Matrix()
        Ts = [[0]*36 for _ in range(36)]
        for i in range(36):
            a= i%6 +1
            b = i//6 +1
            if a !=b and math.gcd(a,b) ==1:
                Sx[i] =1
                for j in range(36):
                    c= j%6 +1
                    d = j//6 +1
                    if c ==b and i !=j and math.gcd(c,d) ==1 and d !=b and d !=a:
                        Ts[i][j] =1
        if n ==1:
            return 6
        elif n ==2:
            return 22
        ret =mxp.dot(mxp.pow(Ts,n-2),Sx)
        #print(ret)
        #return sum(map(lambda x:sum(x),ret))
        return sum(ret)% mxp.mod
        
        
re = Solution().distinctSequences(4)
print(re)