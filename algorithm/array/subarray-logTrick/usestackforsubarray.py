# https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
# more code: contest\00000c361d112\d128\q4
from typing import List, Tuple, Optional



class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        sm = 0
        st =[(10**10,0)]
        for a in nums:
            while st[-1][0] < a:
                st.pop()
            if st[-1][0] ==a :
                a,c = st.pop()
                st.append((a,c+1))
            else:
                st.append((a,1))
            sm += st[-1][1]
        return sm