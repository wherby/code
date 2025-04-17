# 为了枚举 数组中 x*y%k==0的排列数
# 枚举x 求 k2= k/gcd(k, j) 然后把 cnt[k2] 加入
# 然后把x 所有的因子d 加入 cnt
from collections import defaultdict,deque
from math import gcd
# 预处理每个数的因子
MX = 101
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        for j, x in enumerate(nums):  # 枚举 j，计算左边有多少个符合要求的 i
            if j and x == nums[0]:
                ans += 1  # 单独统计 i=0 的情况
            k2 = k // gcd(k, j)  # i 必须是 k2 的倍数
            ans += cnt[(x, k2)]
            for d in divisors[j]:  # j 是 d 的倍数
                cnt[(x, d)] += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-equal-and-divisible-pairs-in-an-array/solutions/1277713/mo-ni-by-endlesscheng-wegn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。