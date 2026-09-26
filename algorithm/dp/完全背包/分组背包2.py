# 这里分组背包的时候 不用 ndp =dp 是因为每次都是从大到小转移，确保了转移来源一定是来自上一轮的值
from collections import defaultdict,deque
from math import inf
class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        f = [0] + [inf] * sum

        for x in nums:
            # 生成这一组的所有物品，相同体积的物品，只保留价值最小的物品
            costs = defaultdict(lambda: inf)
            a = 0
            while x >> a:
                b = 0
                while x >> a << b <= sum:
                    v = x >> a << b
                    costs[v] = min(costs[v], a + b)
                    b += 1
                a += 1

            # 按照体积从小到大排序，方便跳出循环
            items = sorted(costs.items())

            for i in range(sum, 0, -1):
                for v, c in items:
                    if v > i:
                        break
                    f[i] = min(f[i], f[i - v] + c)  # 手写 min 更快，见【Python3 更快的写法】

        return -1 if f[sum] == inf else f[sum]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-operations-to-form-subset-sum-ii/solutions/4019828/fen-zu-bei-bao-by-endlesscheng-eaz3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。