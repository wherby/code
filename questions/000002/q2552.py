# https://leetcode.cn/problems/count-increasing-quadruplets/solutions/2080632/you-ji-qiao-de-mei-ju-yu-chu-li-pythonja-exja/?envType=daily-question&envId=2024-09-10

from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        great =[0]*n 
        great[-1] =[0]*(n+1)
        for k in range(n-2,1,-1):
            great[k] = list(great[k+1])
            for x in range(1,nums[k+1]):
                great[k][x] +=1

        ans = 0
        less = [0]*(n+1)
        for j in range(1,n-1):
            for x in range(nums[j-1] +1, n+1):
                less[x] +=1
            for k in range(j+1,n-1):
                if nums[j]> nums[k]:
                    ans += less[nums[k]] * great[k][nums[j]]
        return ans

re = Solution().countQuadruplets([1,3,2,4,5])
print(re)

