# https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/

from typing import List, Tuple, Optional
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        l,r = [-1]*n,[n]*n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]: 
                r[st[-1]] = i 
                st.pop()
            st.append(i)
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]] <= nums[i]:
                l[st[-1]] = i 
                st.pop()
            st.append(i)
        cnt =0 
        #print(l,r)
        for i in range(n):
            if nums[i] < left or nums[i] > right:continue 
            cnt += (r[i]-i) * ( i-l[i] )
        return cnt

re = Solution().numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8) 
print(re)