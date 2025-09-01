# https://leetcode.cn/problems/sum-of-beautiful-subsequences/description/
# 值域空间压缩

from typing import List, Tuple, Optional
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[{0}] {1}' .format( elapsed, name))
        return result
    return clocked
MOD = 1_000_000_007

# 预处理每个数的因子
MX = 70_001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisors[j].append(i)  # i 是 j 的因子


# 完整模板见 https://leetcode.cn/circle/discuss/mOr1u6/
class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)  # 使用下标 1 到 n

    # a[i] 增加 val
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        t = self.tree
        while i < len(t):
            t[i] += val
            i += i & -i

    # 计算前缀和 a[1] + ... + a[i]
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def pre(self, i: int) -> int:
        t = self.tree
        res = 0
        while i > 0:
            res += t[i]
            i &= i - 1
        return res % MOD


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        m = max(nums)

        # 计算 b 的严格递增子序列的个数
        def count_increasing_subsequence(b: List[int], g: int) -> int:
            t = FenwickTree(m // g)
            res = 0
            for x in b:
                x //= g
                # cnt 表示以 x 结尾的严格递增子序列的个数
                cnt = t.pre(x - 1) + 1  # +1 是因为 x 可以一个数组成一个子序列
                res += cnt
                t.update(x, cnt)  # 更新以 x 结尾的严格递增子序列的个数
            return res

        groups = [[] for _ in range(m + 1)]
        for x in nums:
            for d in divisors[x]:
                groups[d].append(x)

        f = [0] * (m + 1)
        ans = 0
        for i in range(m, 0, -1):
            f[i] = count_increasing_subsequence(groups[i], i)
            # 倍数容斥
            for j in range(i * 2, m + 1, i):
                f[i] -= f[j]
            ans += f[i] * i
        return ans % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sum-of-beautiful-subsequences/solutions/3768197/bei-shu-rong-chi-zhi-yu-shu-zhuang-shu-z-rs5w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from input import nums
re = Solution().totalBeauty(nums )
print(re)