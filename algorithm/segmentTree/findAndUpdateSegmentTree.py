# https://leetcode.cn/problems/fruits-into-baskets-iii/description/
from typing import List, Tuple, Optional

class SegmentTree:
    def __init__(self, a: List[int]):
        n = len(a)
        self.max = [0] * (2 << (n - 1).bit_length())
        self.build(a, 1, 0, n - 1)

    def maintain(self, o: int):
        self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])

    # 初始化线段树
    def build(self, a: List[int], o: int, l: int, r: int):
        if l == r:
            self.max[o] = a[l]
            return
        m = (l + r) // 2
        self.build(a, o * 2, l, m)
        self.build(a, o * 2 + 1, m + 1, r)
        self.maintain(o)

    # 找区间内的第一个 >= x 的数，并更新为 -1，返回这个数的下标（没有则返回 -1）
    def find_first_and_update(self, o: int, l: int, r: int, x: int) -> int:
        if self.max[o] < x:  # 区间没有 >= x 的数
            return -1
        if l == r:
            self.max[o] = -1  # 更新为 -1，表示不能放水果
            return l
        m = (l + r) // 2
        i = self.find_first_and_update(o * 2, l, m, x)  # 先递归左子树
        if i < 0:  # 左子树没找到
            i = self.find_first_and_update(o * 2 + 1, m + 1, r, x)  # 再递归右子树
        self.maintain(o)
        return i


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t = SegmentTree(baskets)
        n = len(baskets)
        ans = 0
        for x in fruits:
            if t.find_first_and_update(1, 0, n - 1, x) < 0:
                ans += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/fruits-into-baskets-iii/solutions/3603049/xian-duan-shu-er-fen-pythonjavacgo-by-en-ssqf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。