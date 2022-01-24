class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        visited = [0]*(n+1)
        cost =[-1]*(n+1)
        st =[(1,0)]
        #visited[1] =1
        g =[[] for _ in range(n+1)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        #print(g)
        def getNumber(c):
            cnt = 0
            sm =0
            while cnt < c:
                if sm  %(change *2) < change:
                    cnt +=1
                    sm += time
                else:
                    sm = (sm //(change*2)  +1)*(change*2)
                #print(sm,cnt)
            return sm
        while st:
            tmp =[]
            for x,c in st:
                if c == cost[x]: continue
                if visited[x] >1:continue
                visited[x] +=1
                cost[x] = c
                #print(x,c,n,visited[x],visited)
                if x == n and visited[x]>1:
                    #print("ccc: ",c)
                    return getNumber(c)
                for b in g[x]:
                    if visited[b] ==2: continue
                    #visited[b] +=1
                    tmp.append((b,c+1))
            st = tmp
        

re =Solution().secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2)
print(re)
