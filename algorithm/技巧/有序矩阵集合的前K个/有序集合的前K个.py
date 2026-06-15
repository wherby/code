
# https://leetcode.cn/problems/maximum-total-subarray-value-ii/solutions/3787892/st-biao-zui-da-dui-pythonjavacgo-by-endl-igja/?envType=daily-question&envId=2026-06-10
# 子数组的特征值可以变成有序集合，则找到前K个就是在有序集合中用堆栈解决

from typing import List, Tuple, Optional


# 手写 min max 更快
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

def op(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return min(a[0], b[0]), max(a[1], b[1])

class ST:
    def __init__(self, a: List[int]):
        n = len(a)
        w = n.bit_length()
        st = [[None] * n for _ in range(w)]
        st[0] = [(x, x) for x in a]
        for i in range(1, w):
            for j in range(n - (1 << i) + 1):
                st[i][j] = op(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])
        self.st = st

    # [l, r) 左闭右开
    def query(self, l: int, r: int) -> int:
        k = (r - l).bit_length() - 1
        mn, mx = op(self.st[k][l], self.st[k][r - (1 << k)])
        return mx - mn

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = ST(nums)

        # 最大堆中保存 (子数组极差，左端点，右端点加一)
        h = [(st.query(i, n), i, n) for i in range(n)]
        # 由于 h 是递减的，无需堆化

        ans = 0
        for _ in range(k):
            d, l, r = h[0]
            if d == 0:  # 堆中剩余元素全是 0
                break
            ans += d
            heapreplace_max(h, (st.query(l, r - 1), l, r - 1))
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-total-subarray-value-ii/solutions/3787892/st-biao-zui-da-dui-pythonjavacgo-by-endl-igja/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。