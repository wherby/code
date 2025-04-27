# https://leetcode.cn/problems/path-existence-queries-in-a-graph-ii/solutions/3663266/pai-xu-shuang-zhi-zhen-bei-zeng-pythonja-ckht/
from typing import List, Tuple, Optional


class DoubleUp:
    def __init__(self, ls,mx = None):
        n = len(ls)
        if mx ==None:
            self.mx =mx=n.bit_length()
        self.dp = [[0]*mx for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = ls[i]
        for i in range(mx-1):
            for x in range(n):
                p = self.dp[x][i]
                self.dp[x][i+1] = self.dp[p][i]
    
    def query(self,l,r):
        ans = 0
        if l >r:
            l,r = r,l
        for k in range(self.mx-1,-1,-1):
            if self.dp[r][k] >l:
                ans += 1<<k 
                r = self.dp[r][k]
        return -1 if self.dp[r][0] > l else ans +1

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        ls = [(a,i) for i,a in  enumerate(nums)]
        ls.sort()
        rord ={}
        nums2 =[]
        for i,(a,idx) in enumerate(ls):
            rord[idx]= i
            nums2.append(a)
        
        dp= [i for i in range(n) ]

        l = 0
        for i,a in enumerate(nums2):
            while a - nums2[l] > maxDiff:
                l +=1
            dp[i] = l
        dup = DoubleUp(dp)
        ans = []
        for l,r in queries:
            if l ==r:
                ans.append(0)
            else:
                l,r = rord[l],rord[r]
                ans.append(dup.query(l,r))
        return ans
        






# re =Solution().pathExistenceQueries( n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]])
# print(re)
re =Solution().pathExistenceQueries( n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]])
print(re)