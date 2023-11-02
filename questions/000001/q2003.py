from typing import List, Tuple, Optional

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        g = [[] for _ in range(n)]
        ret = [1]*n 
        cur = -1
        for i in range(n):
            if nums[i] == 1:
                cur = i 
            if parents[i] != -1:
                g[parents[i]].append(i)
        if cur ==-1:
            return ret 
        cur,val = cur,1 
        visit={}
        vs = {}
        def dfs(a):
            visit[a] = 1
            vs[nums[a]] =1
            #print("A",a,nums[a])
            for b in g[a]:
                if b in visit: continue
                dfs(b)
        #print(g)
        while cur != -1:
            dfs(cur)
            for i in range(val,n+2):
                if i not in vs:
                    val = i 
                    ret[cur] = val 
                    break
            #print(cur,val)
            cur = parents[cur]
            #print(vs,visit,cur)
        return ret



re =Solution().smallestMissingValueSubtree(parents =[-1,0,1,0,3,3], nums = [5,4,6,2,1,3])
print(re)