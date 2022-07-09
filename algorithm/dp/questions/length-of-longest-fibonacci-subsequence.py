# https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/

from collections import defaultdict
from functools import cache
class Solution:
    def lenLongestFibSubseq(self, arr) -> int:
        m = len(arr)
        mx =1
        dic =defaultdict(list)
        for i,a in enumerate(arr):
            dic[a].append(i)
        @cache
        def dfs(a,b):
            c = arr[a] +arr[b]
            mx =0
            if c not in dic:
                return mx
            for x in dic[c]:
                mx = max(mx,1+ dfs(b,x))
            return mx
        for i in range(m):
            for j in range(i+1,m):
                mx = max(mx, 2+dfs(i,j))
        return mx if mx !=2 else 0
    
re =Solution().lenLongestFibSubseq([2,4,5,6,7,8,11,13,14,15,21,22,34])
print(re)
