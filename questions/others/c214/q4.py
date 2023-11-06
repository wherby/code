from sortedcontainers import SortedList
from collections import defaultdict
class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        ls =SortedList()
        dic = defaultdict(int)
        sm =0
        for i,x in enumerate(instructions):
            idx = ls.bisect_left(x)
            idxR = len(ls)- idx -dic[x]
            ls.add(x)
            dic[x]+=1
            sm += min(idx,idxR)
        mod = 10**9 +7
        return sm % mod

re = Solution().createSortedArray(instructions = [1,3,3,3,2,4,2,1,2])
print(re)
