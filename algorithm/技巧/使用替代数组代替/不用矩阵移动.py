# https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/description/?envType=daily-question&envId=2026-03-02
# 这个题目需要一个矩阵移动的贪心解法
# 在涉及矩阵行交换的时候，使用替代数组来记录每行的状态（比如末尾连续0的数量）是一个常见的技巧，可以大大简化代码和逻辑。
# 而在交换的时候，使用冒泡算法式的交换（即每次只交换相邻两行）可以更清晰地计算交换次数，避免直接交换带来的复杂性。
# 记录状态的时候，因为当前行已经处理，所以不用当心当前行的状态 tailZ[i+1:j+1] = tailZ[i:j]，这里移动的是后续行的状态，虽然矩阵的状态不符合但是后续的计算中不符合的区域不会被处理到，所以不影响结果。
from typing import List, Tuple, Optional


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tailZ = [n]*n
        for i in range(n):
            for j in range(n-1,-1,-1):
                if grid[i][j]:
                    tailZ[i] = n-1-j 
                    break
        ans = 0 
        for i in range(n-1):
            need_zero = n-1-i 
            for j in range(i,n):
                if tailZ[j] >= need_zero:
                    ans += j-i 
                    tailZ[i+1:j+1] = tailZ[i:j]
                    break
            else:
                return -1 
        return ans