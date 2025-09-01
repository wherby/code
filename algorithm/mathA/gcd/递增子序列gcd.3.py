# https://leetcode.cn/problems/sum-of-beautiful-subsequences/description/
# 把 fenwicktree 变成函数，也不能减少太多时间。 compare to algorithm/mathA/gcd/递增子序列gcd.py

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

class Solution:
    @clock
    def totalBeauty(self, nums: List[int]) -> int:
        m = max(nums)

        # 树状数组（时间戳优化）
        tree = [0] * (m + 1)
        time = [0] * (m + 1)
        now = 0

        def update(i: int, val: int) -> None:
            nonlocal now
            while i <= m:
                if time[i] < now:
                    time[i] = now
                    tree[i] = 0  # 懒重置
                tree[i] += val
                i += i & -i

        def pre(i: int) -> int:
            res = 0
            while i > 0:
                if time[i] == now:
                    res += tree[i]
                i &= i - 1
            return res % MOD

        # 计算 b 的严格递增子序列的个数
        def count_increasing_subsequence(b: List[int]) -> int:
            nonlocal now
            now += 1  # 重置树状数组（懒重置）
            res = 0
            for x in b:
                # cnt 表示以 x 结尾的严格递增子序列的个数
                cnt = pre(x - 1) + 1  # +1 是因为 x 可以一个数组成一个子序列
                res += cnt
                update(x, cnt)  # 更新以 x 结尾的严格递增子序列的个数
            return res

        groups = [[] for _ in range(m + 1)]
        for x in nums:
            for d in divisors[x]:
                groups[d].append(x)

        f = [0] * (m + 1)
        ans = 0
        for i in range(m, 0, -1):
            f[i] = count_increasing_subsequence(groups[i])
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