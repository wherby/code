from typing import List, Tuple, Optional
from math import comb

from scipy.signal import convolve

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
        c0 = cnt[0]
        cnt[0] = 0

        # 计算 cnt 的自卷积
        cnt2 = convolve(cnt, cnt).astype(int).tolist()

        m = len(nums) - c0  # nums 中的正整数个数
        ans = comb(m, 3)
        s = 0  # a+b <= c 的 (a,b) 的方案数
        for c in range(1, mx + 1):
            c2 = cnt2[c]
            if c % 2 == 0:
                c2 -= cnt[c // 2]  # (c/2,c/2) 算了两次
            s += c2 // 2  # (a,b) 和 (b,a) 各算了一次
            ans -= s * cnt[c]  # 减去 a+b <= c 的 (a,b,c) 的方案数
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/valid-triangle-number/solutions/2432875/zhuan-huan-cheng-abcyong-xiang-xiang-shu-1ex3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。