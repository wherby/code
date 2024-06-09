from typing import List, Tuple, Optional

import heapq
class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        mod = 10**9+7
        n = len(nums)
        nums = [a-i for i,a in enumerate(nums)]
        ret = []
        left,right= [], []
        leftSm ,righSm = 0,0
        for i,a in enumerate(nums):
            if len(right)==0 or a >= right[0]:
                righSm += a 
                heapq.heappush(right,a)
            else:
                leftSm +=a 
                heapq.heappush(left,(-a))
            while len(left)> len(right):
                a = heapq.heappop(left)
                heapq.heappush(right,-a)
                leftSm -=-a
                righSm += -a 
            while len(right) > len(left)+1:
                a = heapq.heappop(right)
                heapq.heappush(left, -a)
                leftSm +=a 
                righSm -=a 
            tmp = 0
            if len(right):
                tmp = righSm - (right[0])*len(right) 
            if len(left):
                tmp += right[0]* len(left) -leftSm
            ret.append(tmp%mod)
            #print(left,right,tmp, leftSm,righSm)
        return ret

re = Solution().numsGame([1,1,1,2,3,4])
print(re)