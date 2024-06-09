# pic/presum.png
#因为多1列表示从 [(x1,y1),(x2,y2)] 双闭区间的query
#对于m*n矩阵 第i行 query(i,0,i,n-1) 
#           第j列 query(0,j,m-1,j) contest/00000c315d89/d92/q2/t2.py
class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c

arr = [[1+i]*10 for i in range(10) ]
print(arr)
pre= Presum2d(arr)
print(pre.pre)
print(pre.query(0,0,9,9))
arr =[[1,0],[0,1]]
pre = Presum2d(arr)
print(pre.query(0,0,0,1))