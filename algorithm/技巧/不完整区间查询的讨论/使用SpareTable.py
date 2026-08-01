from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left

from itertools import pairwise

class SparseTable:
    def __init__(self, a: List[Tuple[int, int]]):
        n = len(a) - 1
        m = n.bit_length()
        st = [[r1 - l1 + r2 - l2] + [0] * (m - 1) for (l1, r1), (l2, r2) in pairwise(a)]
        for j in range(1, m):
            for i in range(n - (1 << j) + 1):
                st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        self.st = st

    # [l,r) 左闭右开
    def query(self, l: int, r: int) -> int:
        if l >= r:
            return 0
        k = (r - l).bit_length() - 1
        return max(self.st[l][k], self.st[r - (1 << k)][k])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total1 = 0
        # 统计连续 0 段对应的区间（左闭右开）
        a = [(-1, -1)]  # 哨兵
        start = 0
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if s[i] == '1':
                    total1 += i - start + 1
                else:
                    a.append((start, i + 1))  # 左闭右开
                start = i + 1
        a.append((n + 1, n + 1))  # 哨兵

        def calc(x: int, y: int) -> int:
            return x + y if x > 0 and y > 0 else 0

        st = SparseTable(a)
        ans = []
        for ql, qr in queries:
            qr += 1  # 左闭右开
            i = bisect_left(a, ql, key=lambda p: p[0])
            j = bisect_right(a, qr, key=lambda p: p[1]) - 1
            mx = 0
            if i <= j:  # [ql,qr) 中有完整的区间
                mx = max(
                    st.query(i, j),  # 相邻完整区间的长度之和的最大值
                    calc(a[i - 1][1] - ql, a[i][1] - a[i][0]),  # i-1 残缺区间 + i
                    calc(qr - a[j + 1][0], a[j][1] - a[j][0]),  # j+1 残缺区间 + j
                )
            elif i == j + 1:  # [ql,qr) 中有两个相邻的残缺区间
                mx = calc(a[i - 1][1] - ql, qr - a[j + 1][0])  # i-1 残缺区间 + j+1 残缺区间
            ans.append(total1 + mx)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-active-section-with-trade-ii/solutions/3633400/qu-jian-zui-da-zhi-er-fen-cha-zhao-fen-l-n832/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re = Solution().maxActiveSectionsAfterTrade(s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]])
print(re)