# 差分矩阵在后续操作中又变成了前缀和矩阵，比较难理解

from typing import List, Tuple, Optional

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 二维差分
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            diff[r1 + 1][c1 + 1] += 1
            diff[r1 + 1][c2 + 2] -= 1
            diff[r2 + 2][c1 + 1] -= 1
            diff[r2 + 2][c2 + 2] += 1

        # 原地计算 diff 的二维前缀和，然后填入答案
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diff[i + 1][j + 1] += diff[i + 1][j] + diff[i][j + 1] - diff[i][j]
                ans[i][j] = diff[i + 1][j + 1]
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/increment-submatrices-by-one/solutions/2062756/er-wei-chai-fen-by-endlesscheng-mh0h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。