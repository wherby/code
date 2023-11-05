from collections import OrderedDict, defaultdict
class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        inls = [0]*n
        g = [[] for _ in range(n)]
        for a,b in edges:
            inls[b]+=1
            g[a].append(b)
        cand =[]
        for i in range(n):
            if inls[i] ==0:
                cand.append(i)
        mn =[0]
        visited = [0]*n
        res =[]
        def dfs(cur):
            visited[cur] =2
            cor  =colors[cur]
            res.append((cor,0))
            for a in g[cur]:
                if visited[a] ==1:continue
                if visited[a] ==2: return False
                if dfs(a) == False:
                    return False
            visited[cur] =1
            res.append((cor,1))
            return True
        if len(cand) ==0:
            return -1
        for c in cand:
            if dfs(c) == False:
                return -1
        visited = [0]*n
        
        
        def dfs2(cur):
            cor  =colors[cur]
            res.append((cor,0))
            visited[cur] =1
            for a in g[cur]:
                if visited[a] ==0:
                    dfs2(a)
            res.append((cor,1))
        for c in cand:
            dfs2(c)
        mx =0
        dic=defaultdict(int)
        for a,op in res:
            if op ==0:
                dic[a]+=1
                if dic[a] > mx:
                    mx =dic[a]
            else:
                dic[a] -=1
        #print(mx)
        return mx
"nnllnzznn"
[[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]

re = Solution().largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]])
print(re)