from typing import List, Tuple, Optional
from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums )
        ret = n +1 
        dic = defaultdict(list)
        acc = 0
        dic[0].append(n)
        for i in range(n-1,-1,-1):
            acc += nums[i]
            dic[acc%p].append(i)
        cur = 0
        for k,v in dic.items():
            dic[k].sort()
        acc = 0 
        d = bisect_left(dic[0],0)
        if d <len(dic[0]):
                #print(dic[rc],rc,acc,i,dic[rc][d] - i ,d)
            ret = min(ret,dic[0][d]  )
        for i,a in enumerate(nums):
            acc = (acc+ a)% p 
            rc = (p-acc)%p
            d  = bisect_left(dic[rc],i+1)
            if d <len(dic[rc]):
                #print(dic[rc],rc,acc,i,dic[rc][d] - i ,d)
                ret = min(ret,dic[rc][d] - i -1)
        return ret if ret <n else -1

nums =[8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
p = 148
re = Solution().minSubarray(nums,p) 
print(re)