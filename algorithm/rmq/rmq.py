# sparse-table for range maximum query https://www.geeksforgeeks.org/range-maximum-query-using-sparse-table/
from math import log2
class RMQ:
    def __init__(self,arr) -> None:
        self.build_st(arr)
    
    def build_st(self,arr):
        n = len(arr)
        self.n = n
        self.arr = arr
        k = int(log2(self.n)) +1 
        #print(k,self.n,int(log2(self.n)))
        self.st=[[0]*k for _ in range(n)]
        for i in range(self.n):
            self.st[i][0] = arr[i]
        
        i,j =0,1
        for j in range(1,k):
            print(j,self.st)
            for i in range(n-(1<<j)+1):
                self.st[i][j] = max(self.st[i][j-1], self.st[i+(1<<(j-1))][j-1])
    
    def query(self,l,r):
        j = int(log2(r-l +1))
        return max(self.st[l][j],self.st[r-(1<<j)+1][j])


rmq = RMQ([7, 2, 3, 0, 5, 10, 3, 12, 18])
print(rmq.st)

print(rmq.query(0, 4))
print(rmq.query(4, 7))
print(rmq.query(7, 8))