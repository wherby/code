# https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/description/
# Will Timeout https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/submissions/625960607/

from sortedcontainers import SortedList
from typing import List, Tuple, Optional
from bisect import bisect_right,bisect_left
## Merge on continue [[1,1][2,2]] will not merge
class Span():
    def __init__(self,N):
        self.span =SortedList([(i,i) for i in range(N)])
    
    def add(self,left,right):
        leftIdx = bisect_left(self.span,(left,left))
        if leftIdx != 0:
            leftIdx -=1
        if self.span[leftIdx][1] <left:
            leftIdx +=1
        remove=[]
        endIdx = leftIdx
        while  endIdx < len(self.span) and self.span[endIdx][0] <=right :
            remove.append(self.span[endIdx])
            endIdx +=1
        newLeft,newRight = left,right
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            self.span.remove(item)
        self.span.add((newLeft,newRight))


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        span = Span(n)
        l = 0
        for i,a in enumerate(nums):
            while a - nums[l] > maxDiff:
                l +=1

            span.add(l,i)
        dic = {}
        for i,(a,b) in enumerate(span.span):
            for j in range(a,b+1):
                dic[j] =i
        ret = []
        for a,b in queries:
            if dic[a] == dic[b]:
                ret.append(True)
            else:
                ret.append(False)
        return ret

re = Solution().pathExistenceQueries( n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]])
print(re)