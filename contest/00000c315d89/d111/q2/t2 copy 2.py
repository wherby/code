from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import functools


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx = 0
        n = len(str2)
        for c in str1:
            if idx < n and (ord(str2[idx]) - ord(c)) % 26 <= 1:
                idx += 1
        return idx == n

#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/s7qlIZ/view/iluIfU/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




re =Solution().canMakeSubsequence(str1 = "abc", str2 = "ad")
print(re)