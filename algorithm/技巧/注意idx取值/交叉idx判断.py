# 前段和后端要求相应端点，所以把前段的idx+1， 
# 分割点就是从 [m :m*2+1]  
from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        m = n //3 
        pre = [10**20]*n 
        post = [0]*n 
        sl = SortedList([])
        sl2 = SortedList([])
        acc =acc2 =0
        for i in range(n):
            acc += nums[i]
            sl.add(nums[i])
            if len(sl) > m:
                acc -= sl[-1]
                sl.remove(sl[-1])
            if len(sl) == m and i +1<n:
                pre[i+1] = acc
            acc2 += nums[-i-1]
            sl2.add(nums[-i-1])
            if len(sl2) > m:
                acc2 -= sl2[0]
                sl2.remove(sl2[0])
            if len(sl2) == m :
                post[-1-i] = acc2 
        return min(a-b for a,b in zip(pre[m:m*2+1],post[m:m*2+1]))

re = Solution().minimumDifference([7,9,5,8,1,3])
print(re)