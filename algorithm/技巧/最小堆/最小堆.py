from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        ans = 0
        h = []
        for x, ch in zip(nums, s):
            heappush(h, -x)  # 取相反数，把 h 视作最大堆
            if ch == '1':
                ans += -heappop(h)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-score-after-binary-swaps/solutions/3861994/zui-xiao-dui-wei-hu-dong-tai-qian-k-da-j-n6zd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。