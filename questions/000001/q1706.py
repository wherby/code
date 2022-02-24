class Solution:
    def findBall(self, grid) :
        m,n =len(grid),len(grid[0])
        res =[-1]*n
        for i in range(n):
            idx =i
            isG = True
            for j in range(m):
                if grid[j][idx]==1 and idx+1<n and grid[j][idx+1]==1:
                    idx +=1
                elif grid[j][idx] ==-1 and idx-1>=0 and grid[j][idx-1] ==-1:
                    idx -=1
                else:
                    isG =False
                    break
                #print(i,idx)
            if isG:
                res[i]=idx
        return res

re = Solution().findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
print(re)