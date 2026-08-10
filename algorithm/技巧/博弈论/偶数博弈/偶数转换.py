


from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(l,r):
            if l ==r:
                return piles[l]
            return max(piles[l] - dfs(l+1,r), piles[r] - dfs(l,r-1))
        n = len(piles)
        return dfs(0,n-1) >0

# 这个题目中因为是偶数个备选，且只能从边沿选取，所以先选的人可以控制选取所有奇数或者所有偶数的项目
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/stone-game/solutions/3999002/wei-shi-yao-xian-shou-bi-sheng-by-endles-qc0w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。