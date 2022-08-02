from collections import defaultdict,deque
class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        m,n = len(isInfected),len(isInfected[0])
        dirs =[[1,0],[-1,0],[0,1],[0,-1]]
        ret =0
        def bfs(px,py,idx):
            visit={}
            st= deque([(px,py)])
            visit[(px,py)] =1
            while st:
                x,y = st.popleft()
                isInfected[x][y] = idx
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visit and isInfected[nx][ny] ==1:
                        st.append((nx,ny))
        idx = 2
        for i in range(m):
            for j in range(n):
                if isInfected[i][j] ==1:
                    bfs(i,j,idx)
                    idx +=1
        def countNext(px,py,idx):
            visit={}
            cnt =0
            st= deque([(px,py)])
            visit[(px,py)] =1
            while st:
                x,y = st.popleft()
                visit[(x,y)]=1
                isInfected[x][y] = idx
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visit and isInfected[nx][ny] ==idx:
                        st.append((nx,ny))
                    if  0<=nx<m and 0<=ny<n and (nx,ny,x,y) not in visit  and isInfected[nx][ny] ==0:
                        visit[(nx,ny,x,y)]=1
                        cnt +=1 
            return cnt
        def getMax():
            dic ={}
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] >0 and isInfected[i][j] not in dic:
                        re = countNext(i,j,isInfected[i][j])
                        dic[isInfected[i][j]] = re
            mk,mv = 0,0
            for k,v in dic.items():
                if v > mv:
                    mv = v 
                    mk = k 
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == mk:
                        isInfected[i][j] =-1
            return mv
        def nextStatge(px,py,idx):
            visit={}
            st= deque([(px,py)])
            visit[(px,py)] =1
            afq =[]
            while st:
                x,y = st.popleft()
                visit[(x,y)]=1
                isInfected[x][y] = idx
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visit and isInfected[nx][ny] ==idx:
                        st.append((nx,ny))
                    if  0<=nx<m and 0<=ny<n and (nx,ny) not in visit and isInfected[nx][ny] ==0:
                        afq.append((nx,ny))
            for x,y in afq:
                isInfected[x][y] = idx

        m1 = getMax()
        while m1:
            ret += m1
            dic ={}
            for i in range(m):
                for j in range(n):
                    t = isInfected[i][j]
                    if t >0 and t  not in dic:
                        dic[t] =1
                        nextStatge(i,j,t)
            m1 = getMax()
        return ret
            
                    

grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

        
#re = Solution().containVirus(isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]])
re =Solution().containVirus(grid)
print(re)