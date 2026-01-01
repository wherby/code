# https://leetcode.cn/problems/maximum-score-after-binary-swaps/solutions/3861994/zui-xiao-dui-wei-hu-dong-tai-qian-k-da-j-n6zd/
from typing import List, Tuple, Optional


from sortedcontainers import SortedDict,SortedList


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)
        sl= SortedList([])
        sm = 0 
        for i,a in enumerate(s):
            sl.add(nums[i])
            if a =="1":
                sm += sl[-1]
                sl.pop()
            #   print(sl,sm)
        return sm





re =Solution().maximumScore(nums = [2,1,5,2,3], s = "01010")
print(re)