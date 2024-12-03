# https://www.bilibili.com/video/BV1fFB4YGEZY/?spm_id_from=333.999.0.0&vd_source=ca787d3785cbd6247961eba27850fa0c 
# https://leetcode.cn/contest/weekly-contest-425/problems/maximize-sum-of-weights-after-edge-removals/description/
from typing import List, Tuple, Optional

from collections import defaultdict,deque

# DFS 返回子节点不和父节点连接的时候，已经选择了K个子节点的情况的值nc， 和可以与父节点结合选择了k-1个子节点的情况
# inc 存的是，每个子节点如果连接了之后可以得到的增量 

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        dic= defaultdict(list)
        for a,b,c in edges:
            dic[a].append(b)
            dic[b].append(a)
            dic[(a,b)] =dic[(b,a)] =c

        def dfs(a,p):
            ncs = 0
            inc = []
            for b in dic[a]:
                if b == p:continue
                nc,c =  dfs(b,a)
                ncs +=nc 
                if dic[(b,a)] + c -nc >0:
                    inc.append(dic[(b,a)] + c -nc)
            inc.sort(reverse=True)
            return ncs + sum(inc[:k]),ncs + sum(inc[:k-1])
        return max(dfs(0,-1))
            






re =Solution().maximizeSumOfWeights(edges = [[0,1,4],[0,2,2],[2,3,12],[2,4,6]], k = 2)
print(re)