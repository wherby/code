# https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
# https://leetcode.cn/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/solution/san-chong-suan-fa-bao-li-er-fen-da-an-du-k1vd/
# 增长方式
from typing import List, Tuple, Optional

from heapq import heappop,heappush 
class Solution:
    # 373. 查找和最小的 K 对数字
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        while h and len(ans) < k:
            _, i, j = heappop(h)
            ans.append(nums1[i] + nums2[j])  # 数对和
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        a = mat[0][:k]
        for row in mat[1:]:
            a = self.kSmallestPairs(row, a, k)
        return a[-1]