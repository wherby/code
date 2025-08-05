# 用数组模拟双向链表删除，查找左右两边存在的最近邻居
# https://www.bilibili.com/video/BV1BEh3zZEoM/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca787d3785cbd6247961eba27850fa0c
from typing import List, Tuple, Optional
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        cnt = n * (n + 1) // 2
        if cnt < k:  # 全改成星号也无法满足要求
            return -1

        # 数组模拟双向链表
        pre = list(range(-1, n))
        nxt = list(range(1, n + 2))

        for t in range(n - 1, -1, -1):
            i = order[t]
            l, r = pre[i], nxt[i]
            cnt -= (i - l) * (r - i)
            if cnt < k:
                return t
            # 删除链表中的 i
            nxt[l] = r
            pre[r] = l

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-time-to-activate-string/solutions/3741028/er-fen-da-an-pythonjavacgo-by-endlessche-6s8n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。