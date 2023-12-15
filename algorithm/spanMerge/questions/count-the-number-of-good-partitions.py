# 合并区间 
# 用左右标识 合并区间
from typing import List, Tuple, Optional
from collections import defaultdict,deque

mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i,a  in enumerate(nums):
            dic[a].append(i)
        cur = 0
        cnt = 0
        n= len(nums)
        while cur < n:
            end = dic[nums[cur]][-1]
            while cur <= end and cur < n:
                end = max(end,dic[nums[cur]][-1])
                cur +=1
            cnt +=1
        return quickPow(2,cnt-1)