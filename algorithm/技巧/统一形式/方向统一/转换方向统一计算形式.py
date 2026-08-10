# 把DP递推反向思考，变成递推
from typing import List, Tuple, Optional

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        suf_sum = f1 = f2 = f3 = 0
        for val in reversed(stoneValue):
            suf_sum += val
            f1, f2, f3 = suf_sum - min(f1, f2, f3), f1, f2

        diff = f1 - (suf_sum - f1)
        if diff == 0:
            return "Tie"
        return "Alice" if diff > 0 else "Bob"

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/stone-game-iii/solutions/4001520/san-chong-fang-fa-zui-da-hua-de-fen-zhi-4gcvw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。