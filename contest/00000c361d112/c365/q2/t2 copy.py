# https://live.bilibili.com/1315966?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.to_liveroom.0.click&live_from=86002
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0 
        max_diff = 0
        pre_max=0
        for x in nums:
            #把 x当作nums[k]
            ans = max(ans,max_diff *x)
            #把 x 当作 nums[j]
            max_diff = max(max_diff,pre_max-x)
            # 把x 当作 x[i]
            pre_max = max(pre_max,x)
        return ans





re =Solution().maximumTripletValue([12,6,1,2,7])
print(re)