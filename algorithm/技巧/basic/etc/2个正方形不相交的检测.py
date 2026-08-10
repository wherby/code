# https://leetcode.cn/contest/weekly-contest-514/problems/maximum-area-of-two-non-overlapping-square-submatrices/
# 这里不相交的两个等大的正方形检测， 
# 两个不相交的正方形只有两种可能的相对位置： 左右或者上下，利用转向操作，把两个正方形都用上下检测就可以保证完备性
from typing import List, Tuple, Optional




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


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        def f(mat):
            m,n = len(mat),len(mat[0])  
            pre = Presum2d(mat)
            def find(d,px,py):
                for i in range(d-1,m):
                    for j in range(d-1,n):
                        if px !=-1:
                            if px-d+1<=i-d+1 <= px and py-d +1 <=j-d+1 <=py:
                                continue
                            if px-d+1<=i-d+1 <= px and py-d +1 <=j <=py:
                                continue
                            
                        if pre.query(i-d+1,j-d+1,i,j) == d**2:
                            return i,j
                return -1,-1
            
            def verify(d):
                if d ==0:
                    return True
                x,y = find(d,-1,-1)
                #print(x,y,d)
                if x == -1 :
                    return False

                x2,y2 = find(d,x,y)
                #print(d,x,y,x2,y2)
                return x2 != -1 
            l,r = 0, m
            while l <r :
                mid = (l+r+1)>>1
                if verify(mid):
                    l = mid 
                else:
                    r = mid -1
            return l**2
        mat2= list(zip(*mat))
        return max(f(mat),f(mat2))




re =Solution().maxArea(mat = [[0,1,1,1,1,1,1,0],[1,1,1,1,0,1,0,1],[1,1,0,0,1,1,1,1]])
print(re)