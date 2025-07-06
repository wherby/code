# 题目求时间点上联通块数量大于k
# 转换为连接联通块使得联通块数量小于k就好了
from typing import List, Tuple, Optional
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
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
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: -x[2])  # 按照 time 降序排列
    
        u = UnionFind(n)
        for e in edges:
            u.merge(e[0], e[1])
            if u.cc < k:  # 这条边不能留，即移除所有 time <= e[2] 的边
                return e[2]
        return 0  # 无需移除任何边

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-time-for-k-connected-components/solutions/3716407/bing-cha-ji-cong-da-dao-xiao-he-bing-pyt-03qz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。