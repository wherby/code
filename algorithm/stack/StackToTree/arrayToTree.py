# https://www.bilibili.com/video/BV1HKcue9ETm/?spm_id_from=333.999.0.0&vd_source=ca787d3785cbd6247961eba27850fa0c
# https://leetcode.cn/contest/weekly-contest-432/problems/count-non-decreasing-subarrays-after-k-operations/description/
# 利用单调栈把数组建立树 algorithm/stack/StackToTree/pic/pic.png
# g 中每个子节点是比它小的单调子节点 

from typing import List, Tuple, Optional

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        pos_r = [n]* n 
        st = []
        for i,x in enumerate(nums):
            while st and x>= nums[st[-1]]:
                pos_r[st[-1]] = i 
                st.pop()
            if st:
                g[st[-1]].append(i)
            st.append(i)
        print(g,pos_r)
                






re =Solution().countNonDecreasingSubarrays([6,3,2,1,4,5,8,6,3],5)
print(re)