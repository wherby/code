from re import L


class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        inD = [0]*n
        g = [[] for _ in range(n)]
        setG = [[] for _ in range(n)]
        for a,b in edges:
            inD[a] +=1
            inD[b] +=1
            g[a].append(b)
            g[b].append(a)
        root =-1
        for i in range(n):
            if inD[i] ==1:
                root = i
                break
        xorD = [0]*n
        visited =[0]*n
        ordD = [0]*n
        def dfs(i,ord):
            visited[i] =1
            ordD[i]  = ord
            val = nums[i]
            setR = set([i])
            for a in g[i]:
                if visited[a]:continue
                valT,setT = dfs(a,ord+1)
                val = val ^ valT
                setR.update(setT)
            setG[i]=setR
            xorD[i] =val
            return (val,setR)
        m = len(edges)
        def getChild(a,b):
            if ordD[a] < ordD[b]:
                return b 
            else:
                return a
        mx = 10**9
        dfs(root,0)
        for i in range(m):
            for j in range(m):
                RR = xorD[root]
                if i == j : continue
                a =getChild(edges[i][0],edges[i][1])
                b = getChild(edges[j][0],edges[j][1])
                if a not in setG[b] and b not in setG[a]:
                    Ra = xorD[a]
                    Rb =xorD[b]
                    rr = RR ^Ra ^Rb
                    mx = min(mx, max(rr,Ra,Rb) -min(rr,Ra,Rb))
                if a in setG[b]:
                    Ra =xorD[a]
                    rr = RR ^ xorD[b]
                    Rb = xorD[b] ^xorD[a]
                    
                    #print(b,a)
                    mx = min(mx, max(rr,Ra,Rb) -min(rr,Ra,Rb))
                if b in setG[a]:
                    Rb =xorD[b]
                    Ra = xorD[b] ^xorD[a]
                    rr = RR ^xorD[a]
                    mx = min(mx, max(rr,Ra,Rb) -min(rr,Ra,Rb))
                #print(a,b, max(rr,Ra,Rb) -min(rr,Ra,Rb),Ra,Rb,rr)
        return mx
        
re =Solution().minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]])
print(re)