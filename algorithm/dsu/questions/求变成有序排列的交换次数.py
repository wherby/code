from typing import List, Tuple, Optional
# 完整的并查集模板，见我的数据结构题单
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己，大小为 1
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        a = sorted((sum(map(int, str(x))), x, i) for i, x in enumerate(nums))
        n = len(a)
        u = UnionFind(n)
        for i, t in enumerate(a):
            u.merge(i, t[2])
        return n - u.cc

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-swaps-to-sort-by-digit-sum/solutions/3679949/jian-tu-ji-suan-lian-tong-kuai-de-ge-shu-6i2r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。