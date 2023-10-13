from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from math import inf

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        idxs = [i for i in range(n) if s1[i] != s2[i]]
        k = len(idxs)
        if k % 2: return -1
        dp = [inf] * (k + 1)
        dp[0] = 0
        for i in range(k):
            # 这里没有删除指的是没有用第二种操作
            # 如果目前考虑的元素个数为奇数，如果最后一个位置没有被删除，则前面位置都被删除了，那么当前的成本是 dp[i]
            if i % 2 == 0: dp[i+1] = dp[i]
            # 如果目前考虑的元素个数为偶数，如果最后一个位置没有被删除，则需要与前面的某项进行配对删除（第一种操作），那么当前的成本是 dp[i] + x，即前面有位置没被删除的成本 + 这次删除的成本，因为要删去最后两项
            else: dp[i+1] = dp[i] + x
            # 考虑使用第二种操作
            if i: dp[i+1] = min(dp[i+1], dp[i-1] + idxs[i] - idxs[i-1])
        return dp[k]

# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/OSToh6/view/PiqYLj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




#re =Solution().minOperations("101101","000000",6)
#print(re)
re =Solution().minOperations("100010010100111100001110101111100001001101011010100111101011100100011111110001011001001","000001100010010011111101100101111011101110010001001010100101011100011110000111010011010",6)
print(re)