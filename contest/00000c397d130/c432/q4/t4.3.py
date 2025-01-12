# https://www.bilibili.com/video/BV1HKcue9ETm/?spm_id_from=333.999.0.0&vd_source=ca787d3785cbd6247961eba27850fa0c
# https://leetcode.cn/contest/weekly-contest-432/ranking/1/?region=local_v2

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        nums= nums[::-1]
        sl = SortedList([])
        st = []
        lo = 0 
        ans = 0 
        for hi,val in enumerate(nums):
            while st and nums[st[-1]] < val:
                idx = st.pop()
                if idx < lo:
                    continue 
                last  = -1 if not st else st[-1]
                last = max(last,lo-1)
                total = max(0, idx-last) *(val - nums[idx])
                k -=total
            st.append(hi)
            sl.add(val)
            while k <0:
                val = nums[lo]
                lo +=1
                sl.remove(val)
                k += max(0,sl[-1] -val)
            ans += hi -lo +1
            #print(ans)
        return ans

                






re =Solution().countNonDecreasingSubarrays([6,3,2,1,4,5,8,6,3],5)
print(re)