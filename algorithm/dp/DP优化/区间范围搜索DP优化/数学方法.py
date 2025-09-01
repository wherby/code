# https://www.bilibili.com/video/BV1aCaGzWEm4/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca787d3785cbd6247961eba27850fa0c
from math import inf

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0
        if n == k:
            return 1 if z == n else -1

        ans = inf
        # 情况一：操作次数 m 是偶数
        if z % 2 == 0:  # z 必须是偶数
            m = max((z + k - 1) // k, (z + n - k - 1) // (n - k))  # 下界
            ans = m + m % 2  # 把 m 往上调整为偶数

        # 情况二：操作次数 m 是奇数
        if z % 2 == k % 2:  # z 和 k 的奇偶性必须相同
            m = max((z + k - 1) // k, (n - z + n - k - 1) // (n - k))  # 下界
            ans = min(ans, m | 1)  # 把 m 往上调整为奇数

        return ans if ans < inf else -1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-operations-to-equalize-binary-string/solutions/3768129/shu-xue-zuo-fa-pythonjavacgo-by-endlessc-ol6s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。