# https://leetcode.cn/contest/biweekly-contest-110/problems/minimum-time-to-make-array-sum-at-most-x/

from typing import List, Tuple, Optional

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], xx: int) -> int:
        n = len(nums1)
        p = sorted([(nums2[i],nums1[i]) for i in range(n)])
        f = [0]*(n+1)
        for x,y in p: # <= 先对P排序，确保在每个阶段的值是最优解
            for i in reversed(range(n)): # 在n个number中选择m个number在m天使用不同的number产生的收益
                                         # 在m天中一个number只能使用1次，所以是倒序 dp
                f[i+1] = max(f[i+1],f[i] + (i+1)*x+y)
        k = sum(nums2)
        b = sum(nums1)
        for i in range(0,n+1):
            if k*i + b - f[i] <=xx:
                return i
        return -1
        





#re =Solution().minimumTime([1,7,6,2,9],[4,2,3,3,0],23)
re =Solution().minimumTime(nums1 = [1,2,3], nums2 = [1,2,3], xx = 4)
print(re)