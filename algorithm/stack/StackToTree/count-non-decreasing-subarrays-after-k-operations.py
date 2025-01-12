# https://www.bilibili.com/video/BV1HKcue9ETm/?spm_id_from=333.999.0.0&vd_source=ca787d3785cbd6247961eba27850fa0c
# https://leetcode.cn/contest/weekly-contest-432/problems/count-non-decreasing-subarrays-after-k-operations/description/
# 利用单调栈把数组建立树 algorithm/stack/StackToTree/pic/pic.png
# 树的父节点是元素左边大于它的最近节点，
# g 中每个子节点是比它小的单调子节点 

from typing import List, Tuple, Optional
from collections import defaultdict,deque
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
            #左边大于x的最近元素，
            if st:
                g[st[-1]].append(i)
            st.append(i)
        ans = cnt = window_left = 0 
        q = deque([])
        for window_r,x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(window_r)
            cnt += max(nums[q[0]] - x ,0)

            while cnt >k:
                out = nums[window_left]
                for i in g[window_left]:
                    if i > window_r:
                        break
                    cnt -= (out -nums[i])*(min(pos_r[i],window_r + 1) -i)
                window_left +=1

                if q[0]< window_left:
                    q.popleft()
            ans += window_r - window_left +1
        return ans

                






re =Solution().countNonDecreasingSubarrays([6,3,2,1,4,5,8,6,3],5)
print(re)