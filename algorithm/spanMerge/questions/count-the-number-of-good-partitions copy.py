# 合并区间 
# 用左右标识 合并区间
from typing import List, Tuple, Optional

mod = 10**9 +7

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        dic = {}
        for i,a  in enumerate(nums):
            dic[a] =i

        cnt = 0
        end = dic[nums[0]]
        for i,a in enumerate(nums):
            end = max(end,dic[a])
            if i == end:
                cnt +=1
        return pow(2,cnt-1,mod)