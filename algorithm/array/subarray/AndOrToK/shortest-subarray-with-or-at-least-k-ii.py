# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/
# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/submissions/518495080/ complex submissions
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ret = 10**10
        pre = {}
        for i,a in enumerate(nums):
            cur = defaultdict(int)
            pre[a] = i 
            for key,idx in pre.items():
                cur[key|a] = max(pre[key],cur[key|a] )
                if (key |a) >=k: 
                    ret = min(ret,i-cur[key|a]+1)
            pre = cur
        return ret if ret != 10**10 else -1
    
re =Solution().minimumSubarrayLength([53,52,53,50,1,2,51,12],55)
print(re)