# https://leetcode.cn/problems/find-the-most-competitive-subsequence/description/?envType=daily-question&envId=2024-05-24
# 记录最大的pop数，算法比直接写堆排序更简单

from typing import List, Tuple, Optional
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ret = -1
        pops = n-k
        st = [-1] 
        for a in nums:
            while pops and st[-1]> a :
                pops -=1 
                st.pop()
            st.append(a)
        return st[1:1+k]