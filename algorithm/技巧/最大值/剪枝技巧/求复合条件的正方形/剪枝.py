from typing import List, Tuple, Optional
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x

        # 返回左上角在 (r1, c1)，右下角在 (r2, c2) 的子矩阵元素和
        def query(r1: int, c1: int, r2: int, c2: int) -> int:
            return s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]

        ans = 0
        for i in range(m):
            for j in range(n):
                # 边长为 ans+1 的正方形，左上角在 (i, j)，右下角在 (i+ans, j+ans)
                while i + ans < m and j + ans < n and query(i, j, i + ans, j + ans) <= threshold:
                    ans += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solutions/3873775/wu-xu-er-fen-bao-li-mei-ju-jiu-shi-omnpy-r7yk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。