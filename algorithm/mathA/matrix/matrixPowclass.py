# https://leetcode.cn/problems/number-of-distinct-roll-sequences/
# contest\00000c275d69\d81\q4\t42.py

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
    
mx = Matrix()
b =  [[1,1],[1,1]]
print(mx.pow(b,19))