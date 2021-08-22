class Solution:
    def latestDayToCross(self, row, col, cells) :
        mp = []
        for i in range(row+1):
            mp.append([1]+ [0]*(col) +[1])
        index = 0
        for cell in cells:
            index = index +1
            x,y = cell[0],cell[1]
            mp[x][y] = 1
            q=[[x,y+1],[x,y-1],[x+1,y]]
            while len(q) >0:
                t = q.pop()
                if t[0] <=row:
                    if mp[t[0]][t[1]] ==0 and mp[t[0]-1][t[1]] ==1 and mp[t[0]][t[1]+1]==1 and mp[t[0]][t[1]-1] ==1:
                        q.append([t[0],t[1]+1])
                        q.append([t[0],t[1]-1])
                        q.append([t[0]+1,t[1]])
                        mp[t[0]][t[1]] =1
            x =filter(lambda x : mp[row][x] ==1, range(col+2))
            if(len(list(x)) == col +2):
                print(index)
                return index-1
            print(mp)
        print(mp)

                        
row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]
Solution().latestDayToCross(row,col,cells)

        