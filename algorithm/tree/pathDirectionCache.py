# https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/
# 注意到节点值都为正，所以最短路径必然只有一个点，且最长路径必定链接两个出入度为1的节点（叶节点），
# 因此我们只需求解从叶节点1到叶节点2去掉其中较小叶节点的路径值即可。这里考虑对边AB使用记忆化搜索，
# 探索以节点A为起点朝节点B走能获得的最大路径值，由于每条边最多计算正反两次（从A走到B或者从B走到A）
# ，搜索总量是 O(n)O(n)

#作者：sandytan2
#链接：https://leetcode.cn/circle/discuss/IAQlrp/view/tUE4ty/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List, Tuple, Optional

from functools import cache


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g=  [[] for _ in range(n)]
        ind = [0]*n 
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            ind[a] +=1
            ind[b] +=1
        ret = 0
        @cache
        def dfs(node,parent):
            nonlocal ret
            res = 0
            for i in g[node]:
                if i == parent: continue
                res = max(res,dfs(i,node))
            ret = max(ret,res)
            return res + price[node]
        for i in range(n):
            if ind[i] ==1:
                dfs(i,-1)
        return ret