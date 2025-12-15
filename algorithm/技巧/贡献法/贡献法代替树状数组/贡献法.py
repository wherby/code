# https://leetcode.com/contest/weekly-contest-479/problems/total-score-of-dungeon-runs/description/
# 对于位置i, 从j 开始的时候 hp - (s[i+1] - s[j]) >= req 的时候得分
# 则 变形 s[j] >= req + s[i+1] - hp， 右边是对于i而言是固定值，所以需要 s[j] 大于次值，并且 j <=i 的个数

from typing import List, Tuple, Optional
from bisect import bisect_right,insort_left,bisect_left



class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        s = [0] * (len(damage) + 1)
        ans = 0
        for i, (dmg, req) in enumerate(zip(damage, requirement)):
            s[i + 1] = s[i] + dmg
            low = s[i + 1] + req - hp
            j = bisect_left(s, low, 0, i + 1)  # 在 [0, i] 中二分
            ans += i - j + 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/total-score-of-dungeon-runs/solutions/3850868/gong-xian-fa-qian-zhui-he-er-fen-cha-zha-uwu2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。