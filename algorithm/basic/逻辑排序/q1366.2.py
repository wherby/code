# https://leetcode.cn/problems/rank-teams-by-votes/solutions/3020274/zi-ding-yi-pai-xu-jian-ji-xie-fa-pythonj-de1p/?envType=daily-question&envId=2024-12-29

from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m = len(votes[0])
        cnts = defaultdict(lambda: [0] * m)
        for vote in votes:
            for i, ch in enumerate(vote):
                cnts[ch][i] -= 1  # 改成负数（相反数），方便比大小
        return ''.join(sorted(cnts, key=lambda ch: (cnts[ch], ch)))

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/rank-teams-by-votes/solutions/3020274/zi-ding-yi-pai-xu-jian-ji-xie-fa-pythonj-de1p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。