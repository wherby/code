# https://leetcode.cn/problems/shortest-path-in-a-weighted-tree/description/?slug=number-of-unique-xor-triplets-i&region=local_v2

from typing import List, Tuple, Optional

from collections import defaultdict,deque
import math
INF  = math.inf

class NumArray:
    def __init__(self, nums: List[int]):
        self.raw = [t for t in nums]
        T = 2
        while T <= len(nums) :
            for i in range(T, len(nums)+1, T) :
                nums[i-1] += nums[i-1-T//2]
            T = T * 2
        self.nums = nums
        self.lowbit = lambda x : x&(-x)

    def update(self, index: int, val: int) -> None:
        if val == self.raw[index] :
            return
        dis = val - self.raw[index]
        self.raw[index] = val
        while index < len(self.nums) :
            self.nums[index] += dis
            index += self.lowbit(index+1)

    def presums(self, index) :
        to_ret = 0
        while index >= 0 :
            to_ret += self.nums[index]
            index -= self.lowbit(index+1)
        return to_ret

    def sumRange(self, left: int, right: int) -> int:
        return self.presums(right)-self.presums(left-1)

class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n+1)]
        dic = defaultdict(int)
        for a,b,c in edges:
            g[a].append(b)
            g[b].append(a)
            dic[(a,b)] =c 
            dic[(b,a)] =c 
        ord =[]
        dic2=defaultdict(list)
        depth = [0]*(n+1)

        stk = [1]
        parent =[-1]*(n+1)
        while stk:
            u = stk.pop()
            if u >= 0:
                if parent[u] != -1:
                    depth[u] = depth[parent[u]] +1
                    ord.append((parent[u],u))
                stk.append(~u)
                for v in g[u]:
                    if parent[u]!=v:
                        parent[v] = u 
                        stk.append(v)
            else:
                u =~u
                if parent[u] != -1:
                    ord.append((u,parent[u]))
        #print(ord,depth)
        ls=[]
        
        for i,(a,b) in enumerate(ord):
            if depth[a] < depth[b]:
                ls.append(dic[(a,b)])
                dic2[b].append(i)
            else:
                ls.append(-dic[(a,b)])
                dic2[a].append(i)
        #print(ls,dic2)
        ans = []
        ft = NumArray(ls)
        for query in queries:
            if query[0] ==1:
                _,a,b, c = query
                if depth[a] >depth[b]:
                    a,b =b,a
                e,f= dic2[b]
                ft.update(e,c)
                ft.update(f,-c)
            else:
                _,b =query
                e,f =dic2.get(b,(-1,-1))
                ans.append(ft.sumRange(0,e))
        return ans



re =Solution().treeQueries(  n = 3, edges = [[1,2,2],[1,3,4]], queries = [[2,1],[2,3],[1,1,3,7],[2,2],[2,3]])
print(re)