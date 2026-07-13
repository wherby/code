# https://leetcode.cn/contest/weekly-contest-510/problems/create-grid-with-exactly-k-paths-i/

class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        grid = [["#"]*n for _ in range(m)]
        lastx,lasty =0,0
        if k == 1:
            lastx = 0
        if k ==2 or k ==3 :
            if min(m,n) <2 or max(m,n)<k:
                return []
            for i in range(2):
                for j in range(2):
                    grid[i][j] = "."
            lastx,lasty = 1,1 
            if k == 3:
                if m >2:
                    for j in range(2):
                        grid[2][j] ="."
                        lastx =2 
                else:
                    for j in range(2):
                        grid[j][2] = "."
                        lasty =2 
        if k ==4:
            if m>=3 and n >=3:
                lastx,lasty =2,2 
                for i in range(3):
                    for j in range(3):
                        grid[i][j] = "."
                grid[0][2]=grid[2][0] = "#"
            elif max(m,n) >=4 and min(m,n)>=2:
                lastx,lasty =1,1
                for i in range(2):
                    for j in range(2):
                        grid[i][j] = "."
                if m >=4:
                    for j in range(2):
                        grid[2][j] ="."
                        grid[3][j]="."
                        lastx =3 
                else:
                    for j in range(2):
                        grid[j][2] = "."
                        grid[j][3] = "."
                        lasty =3
            else:
                return [] 
        #print(grid,lastx,lasty)
        for i in range(lastx,m):
                grid[i][lasty] = "."
        for j in range(lasty,n):
            grid[m-1][j] = "."
        grid = ["".join(arr) for arr in grid]
        return grid





re =Solution().createGrid(4,2,4)
print(re)