from collections import defaultdict
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        
        n = len(favorite)
        dsu = DSU(n)
        g = [[] for _ in range(n)]
        for i,a in enumerate(favorite):
            g[a].append(i)
            dsu.union(i,a)
        d =[0]*n
        for i in range(n):
            d[i] = dsu.find(i)
        #print(d)
        cnt = [0] * n
        visited =[0]*n
        def dfs(x,c):
            if visited[x] == 1:
                return 0
            if cnt[x] != 0:
                return cnt[x]
            visited[x] =1
            mx =0
            for a in g[x]:
                if visited[a] ==0:
                    mx= max(mx,dfs(a,0))
            cnt[x] = c + mx +1
            #visited[x] =0
            z = cnt[x]
            #cnt[x] =0
            return z
        mx = 0
        dic=defaultdict(int)
        for i in range(n):
            if  favorite[ favorite[i]] ==i and visited[i] ==0:
                k = dsu.find(i)
                visited[favorite[i]]=1
                t1 = dfs(i,1)
                if t1 > dic[k]:
                    dic[k] +=t1
                visited[favorite[i]]=0
                t2 = dfs(favorite[i],-1)
                visited[favorite[i]]=1
                #print(t2)
                dic[k] +=t2
                #print(visited)
                mx += dic[k]
        #print(dic)
        visited =[0]*n
        cnt =[0] *n
        #print(mx)
        def dfs2(i):
            if visited[favorite[i]] ==1:
                cnt[i]  = cnt[favorite[i]] +1
            else:
                visited[favorite[i]] =1
                cnt[favorite[i]]= dfs2(favorite[i])
                cnt[i]  = cnt[favorite[i]] +1
            return cnt[i]
            
        for i in range(n):
            dfs2(i)
        for i in range(n):
            mx = max(mx, cnt[favorite[i]]-cnt[i]+1)

        return mx
            
            
        

re = Solution().maximumInvitations(favorite = [1,2,0])
print(re)
        