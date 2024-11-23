from typing import List, Tuple, Optional
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cnt = 0 
        if m%2 ==1 and n %2 ==1:
            cnt +=grid[m//2][n//2]
        for i in range(m//2):
            for j in range(n//2):
                acc = grid[i][j] + grid[m-1-i][j] + grid[m-1-i][n-1-j] + grid[i][n-1-j]
                cnt += min(acc%4, (4-acc)%4)
        acc =0
        diff =0
        if m%2==1:
            t= (m)//2
            for i in range(n//2):
                if grid[t][i] == grid[t][n-1-i]:
                    acc += grid[t][i]*2
                else:
                    acc +=1
                    diff +=2
        if n %2 ==1:
            t = (n)//2
            for i in range(m//2):
                #print(i,t,m,n,m-1-i)
                if grid[i][t] == grid[m-1-i][t]:
                    acc += grid[i][t]*2 
                else:
                    acc +=1
                    diff +=2
        if diff ==0:
            return cnt + acc%4
        else:
            return cnt + diff //2
        
re = Solution().minFlips(grid = [[0,0,0],[1,1,0],[0,1,1],[0,0,1]])
print(re)

# [0,0,0],
# [1,1,0],
# [0,1,1],
# [0,0,1