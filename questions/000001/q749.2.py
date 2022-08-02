from collections import defaultdict,deque
class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        dirs =[[1,0],[-1,0],[0,1],[0,-1]]
        #print(isInfected)
        m,n = len(isInfected),len(isInfected[0])
        
        ret =0
        def bfs(px,py,idx):
            visit={}
            st= deque([(px,py)])
            while st:
                x,y = st.popleft()
                if (x,y) in visit:continue
                visit[(x,y)]=1
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
            cnt2 =0
            st= deque([(px,py)])
            while st:
                x,y = st.popleft()
                if (x,y) in visit:continue
                visit[(x,y)]=1
                isInfected[x][y] = idx
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy 
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visit and isInfected[nx][ny] ==idx:
                        st.append((nx,ny))
                    if  0<=nx<m and 0<=ny<n and (nx,ny,x,y) not in visit  and isInfected[nx][ny] ==0:
                        visit[(nx,ny,x,y)]=1
                        cnt +=1 
                    if  0<=nx<m and 0<=ny<n and (nx,ny) not in visit  and isInfected[nx][ny] ==0:
                        visit[(nx,ny)]=1
                        cnt2 +=1
            return (cnt,cnt2)
        def getMax():
            dic ={}
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] >0 and isInfected[i][j] not in dic:
                        re1, re = countNext(i,j,isInfected[i][j])
                        dic[isInfected[i][j]] = re1,re
            mk,mv,mv2 = 0,0,0
            for k,(v1,v) in dic.items():
                if v > mv:
                    mv = v 
                    mv2 =v1
                    mk = k 
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == mk:
                        isInfected[i][j] =-1
            return mv2
        def nextStatge(px,py,idx):
            visit={}
            st= deque([(px,py)])
            afq =[]
            while st:
                x,y = st.popleft()
                if (x,y) in visit:continue
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
        dic ={}
        for i in range(m):
                for j in range(n):
                    t = isInfected[i][j]
                    if t >0 and t  not in dic:
                        dic[t] =1
                        nextStatge(i,j,t)
        for i in range(m):
            for j in range(n):
                if isInfected[i][j] > 0:
                    isInfected[i][j] =1
        #print(m1,isInfected)
        return m1+ self.containVirus(isInfected) if m1 !=0 else 0
            
                    

grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
grid=[[0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1],[0,0,0,1,0,1,0,1,1,1],[0,1,0,0,1,0,0,1,1,0],[0,1,0,1,0,0,0,1,1,0],[0,1,1,0,0,1,1,0,0,1],[1,0,1,1,0,1,0,1,0,1]]
grid =[[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]] 
#re = Solution().containVirus(isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]])
re =Solution().containVirus(grid)
print(re)