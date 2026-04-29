from typing import List, Tuple, Optional

from sortedcontainers import SortedList

class DominanceSet:
    def __init__(self):
        # 存储 (x, y)，保证 x 递增时 y 递增
        self.points = SortedList()

    def update(self, x, y):
        # 1. 寻找插入位置：找到第一个数值 >= x 的点
        idx = self.points.bisect_left((x, -float('inf')))
        
        # 2. 支配检查：如果前一个点（数值更小）的得分已经比你高，你就是无效点
        if idx > 0 and self.points[idx-1][1] >= y:
            return
        
        # 3. 剔除：如果你比后面那些（数值更大）的点得分还高，那些点就没意义了
        while idx < len(self.points) and self.points[idx][1] <= y:
            self.points.pop(idx)
            
        self.points.add((x, y))

    def query(self, x):
        """查询所有满足 x_prev < x 的点中，最大的 y"""
        idx = self.points.bisect_left((x, -float('inf')))
        if idx > 0:
            return self.points[idx-1][1]
        return -float('inf')

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0: return 0
        
        # 两个支配集：
        # ds_for_up: 存波谷(down)状态，用于更新波峰(up)，要求 nums[j] < nums[i]
        # ds_for_down: 存波峰(up)状态，用于更新波谷(down)，要求 nums[j] > nums[i]
        ds_for_up = DominanceSet()
        ds_for_down = DominanceSet() # 通过存 -val 来实现“大于”查询

        up = [0] * n
        down = [0] * n
        ans = 0
        
        for i in range(n):
            val = nums[i]
            
            # 维护距离限制 k
            if i >= k:
                prev = i - k
                ds_for_up.update(nums[prev], down[prev])
                ds_for_down.update(-nums[prev], up[prev])
            
            # 基础得分（子序列长度为 1）
            curr_up = val
            curr_down = val
            
            # 1. 作为波峰：找之前更小的波谷
            prev_down_max = ds_for_up.query(val)
            if prev_down_max != -float('inf'):
                curr_up = max(curr_up, prev_down_max + val)
            
            # 2. 作为波谷：找之前更大的波峰 (即 -val_prev < -val)
            prev_up_max = ds_for_down.query(-val)
            if prev_up_max != -float('inf'):
                curr_down = max(curr_down, prev_up_max + val)
            
            up[i], down[i] = curr_up, curr_down
            ans = max(ans, curr_up, curr_down)
            
        return ans


nums = [1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000,100000,1,50000]
k =5


re =Solution().maxAlternatingSum( nums , k )
print(re)