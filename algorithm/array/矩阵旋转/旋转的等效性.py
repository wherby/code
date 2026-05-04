# 把旋转分解为两个动作，先沿x=y轴线翻转，然后每行reverse
from typing import List, Tuple, Optional
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 第一步：转置
        for i in range(n):
            for j in range(i):  # 遍历对角线下方元素
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：行翻转
        for row in matrix:
            row.reverse()

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/rotate-image/solutions/3655166/shu-xue-ben-zhi-liang-ci-fan-zhuan-deng-aon4a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。