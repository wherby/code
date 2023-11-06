
class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        res =[]

        def getList(startx,stary, endx,endy):
            re =[]
            x,y = startx,stary
            while x <endx:
                re.append([y,x])
                x +=1
            
            while y < endy:
                re.append([y,x])
                y +=1
            while x >startx:
                re.append([y,x])
                x -=1
            while y >stary:
                re.append([y,x])
                y-=1
            return re
        sx,sy,ex,ey = 0,0,n-1,m-1
        for  i in range(min(m//2,n//2)):
            re = getList(sx,sy,ex,ey)
            res.append(re)
            sx,sy,ex,ey =sx+1,sy+1,ex-1,ey-1 
        rmx = [[0]*n for _ in range(m)]
        for re in res:
            le = len(re)
            #print(le,res)
            kt = k% le
            for i in range(le):
                endIDX = (i +kt + le) %le
                startI = re[i]
                endI= re[endIDX]
                rmx[startI[0]][startI[1]] = grid[endI[0]][endI[1]]
        #print(rmx)
        return rmx
                
                

re =Solution().rotateGrid(grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2)