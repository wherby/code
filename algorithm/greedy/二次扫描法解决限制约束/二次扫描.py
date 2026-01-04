from typing import List, Tuple, Optional


from math import inf

class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        max_val = [inf] * n
        for i, mx in restrictions:
            max_val[i] = mx

        a = [0] * n
        for i, d in enumerate(diff):
            a[i + 1] = min(a[i] + d, max_val[i + 1])
        for i in range(n - 2, 0, -1):
            a[i] = min(a[i], a[i + 1] + diff[i])
        return max(a)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-maximum-value-in-a-constrained-sequence/solutions/3872153/liang-ci-sao-miao-fa-pythonjavacgo-by-en-p7qc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。