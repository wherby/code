# https://leetcode.cn/problems/maximum-path-intersection-sum-in-a-grid/
# 如果包含边界的点，则至少要有2的长度，如果包含中间的点，则可以只包含1的长度
# 转换为求至少2长度的区域的和

from typing import List, Tuple, Optional
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        def maxV(arr):
            ret = -10**10
            cur = arr[0]

            for a in arr[1:]:
                cur += a 
                if ret < cur :
                    ret = cur 
                if cur < a:
                    cur = a 
            return ret 
        ret = -10**10
        for i in range(1,m-1):
            for j in range(1,n-1):
                ret = max(ret,grid[i][j])

        for arr in grid:
            ret = max(ret,maxV(arr))
        
        for arr in list(zip(*grid)):
            ret = max(ret,maxV(arr))
        return ret