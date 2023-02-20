# bisect

##
from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return sum(bisect_right(nums,upper - x,0,i) - bisect_left(nums,lower - x,0,i) for i,x in enumerate(nums))

#作者：雪景式
#链接：https://leetcode.cn/circle/discuss/Auxj4T/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。