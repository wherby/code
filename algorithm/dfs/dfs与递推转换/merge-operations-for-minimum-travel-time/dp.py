# 在递推的时候保存了pre节点
from typing import List, Tuple, Optional

from itertools import accumulate
from math import inf

class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        s = list(accumulate(time, initial=0))
        f = [[[inf] * n for _ in range(n)] for _ in range(k + 1)]
        f[0][-1] = [0] * n
        for left_k in range(k + 1):
            for i in range(n - 2, -1, -1):
                for pre in range(i + 1):
                    t = s[i + 1] - s[pre]
                    f[left_k][i][pre] = min(f[left_k - (nxt - i - 1)][nxt][i + 1] + (position[nxt] - position[i]) * t
                                            for nxt in range(i + 1, min(n, i + 2 + left_k)))
        return f[k][0][0]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/merge-operations-for-minimum-travel-time/solutions/3668454/hua-fen-xing-dpcong-ji-yi-hua-sou-suo-da-cref/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。