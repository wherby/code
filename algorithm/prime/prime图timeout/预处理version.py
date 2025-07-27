# https://leetcode.cn/contest/weekly-contest-460/problems/minimum-jumps-to-reach-end-via-prime-teleportation/submissions/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
# 预处理每个数的质因子列表
mx = 1000001
PRIME_FACTORS = [[] for _ in range(mx)]
for i in range(2, mx):
    if not PRIME_FACTORS[i]:  # i 是质数
        for j in range(i, mx, i):  # i 的倍数有质因子 i
            PRIME_FACTORS[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            for p in PRIME_FACTORS[x]:
                groups[p].append(i)

        ans = 0
        vis = [False] * n
        vis[0] = True
        q = [0]

        while True:
            tmp = q
            q = []
            for i in tmp:
                if i == n - 1:
                    return ans
                idx = groups[nums[i]]
                idx.append(i + 1)
                if i:
                    idx.append(i - 1)
                for j in idx:
                    if not vis[j]:
                        vis[j] = True
                        q.append(j)
                idx.clear()
            ans += 1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-jumps-to-reach-end-via-prime-teleportation/solutions/3734792/bfspythonjavacgo-by-endlesscheng-bu60/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。