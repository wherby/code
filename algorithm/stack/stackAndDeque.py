# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pls = [0]*(n+1)
        for i in range(n):
            pls[i+1] = pls[i] + nums[i]
        st = deque([])
        res = 10**7
        for i,curSum in enumerate(pls):
            while st and  curSum - pls[st[0]] >=k:
                res = min(res, i - st.popleft())
            while st and pls[st[-1]] >= curSum:
                st.pop()
            st.append(i)
        return res if res != 10**7 else -1
