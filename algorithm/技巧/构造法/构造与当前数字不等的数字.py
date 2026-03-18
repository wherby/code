# https://leetcode.cn/problems/find-unique-binary-string/solutions/951165/go-jian-ji-xie-fa-by-endlesscheng-mcwc/?envType=daily-question&envId=2026-03-08
# 题目中有特殊情况，位数等于个数
from typing import List, Tuple, Optional


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = [''] * len(nums)
        for i, s in enumerate(nums):
            ans[i] = '1' if s[i] == '0' else '0'
        return ''.join(ans)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-unique-binary-string/solutions/951165/go-jian-ji-xie-fa-by-endlesscheng-mcwc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。