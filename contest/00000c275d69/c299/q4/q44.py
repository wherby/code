# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/discuss/2199740/Python-One-pass-DFS-%2B-Hashset-easy-to-understand-(with-pics)
from functools import reduce
from collections import defaultdict
class Solution:
    def minimumScore(self, nums, edges) -> int:
        s = reduce(lambda x,y:x^y, nums)
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        self.res = float('inf')
        
        def calc_res(a,b,c):
            return max(a,b,c) - min(a,b,c)
        
        def dfs(root,parent,others):
            subtrees = set()
            cur = nums[root]
            for i in adj[root]:
                if i!=parent:
                    v, children = dfs(i,root,others|subtrees)
                    subtrees |= children
                    cur ^= v
			
            for other in others:
                self.res = min(self.res,calc_res(cur,other,s^cur^other))
            if parent!=-1:
                for child in subtrees:
                    self.res = min(self.res,calc_res(cur^child,s^cur,child))
            subtrees.add(cur)
            return cur,subtrees
        
        dfs(0,-1,set())
        
        return self.res


        
re =Solution().minimumScore([9,14,2,1],[[2,3],[3,0],[3,1]])
print(re)