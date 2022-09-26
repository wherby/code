from collections import defaultdict


class Solution(object):
    def ballGame(self, num, plate):
        """
        :type num: int
        :type plate: List[str]
        :rtype: List[List[int]]
        """
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(plate),len(plate[0])
        visited=[[0]*n for _ in range(m)]
        
        def nextDir(dir, x,y):
            if plate[x][y] == "E":
                for k,d in enumerate(dirs):
                    if d ==dir:
                        return dirs[(k+1)%4]
            elif plate[x][y] =="W":
                for k,d in enumerate(dirs):
                    if d ==dir:
                        return dirs[(k-1 +4)%4]
            return dir
        badDic={}
        goodDic={}
        def visit(dir,x,y):
            dic=defaultdict(int)
            #seed = (x,y)
            for i in range(num):
                nx,ny = x+dir[0], y+ dir[1]
                if nx==-1 or ny ==-1 or nx==m or ny==n:
                    for k,v in dic.items():
                        badDic[k]=1
                    return False
                if (x,y,dir[0],dir[1]) in badDic:
                    return False
                if (x,y,dir[0],dir[1]) in goodDic:
                    if num -i >goodDic[(x,y,dir[0],dir[1])]:
                        return True
                    else:
                        return False
                if plate[nx][ny] =="O":
                    for k,v in dic.items():
                        goodDic[k] = i+1-v
                    return True
                dic[(x,y,dir[0],dir[1])] =i+1
                dir = nextDir(dir,nx,ny)
                x,y = nx,ny
                if dic[(x,y,dir[0],dir[1])] >1 or (x,y,dir[0],dir[1]) in badDic:
                    for k,v in dic.items():
                        badDic[k]=1
                    return False
            return False
        
        res =[]
        cands =[]
        for i in range(1,n-1):
            if plate[0][i] ==".":
                cands.append(([1,0] ,0,i))
            if plate[m-1][i] ==".":
                cands.append(([-1,0] ,m-1,i))
        for i in range(1,m-1):
            if plate[i][0] ==".":
                cands.append(([0,1],i,0))
            if plate[i][n-1] ==".":
                cands.append(([0,-1],i,n-1))
        for dir,x,y in cands:
            if visit(dir,x,y):
                res.append([x,y])
        return res
            





re =Solution().ballGame(3,[".....","....O","....O","....."])
re =Solution().ballGame(5,[".....","..E..",".WO..","....."])
print(re)