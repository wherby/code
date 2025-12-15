from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        def min_operations_to_nonnegative(arr):
            n = len(arr)
            if n == 0:
                return 0
            
            total = sum(arr)
            if total < 0:
                return -1  # 不可能全非负
            
            # 平均值
            mu = total / n
            
            # 计算差值前缀和
            prefix = [0] * n
            prefix[0] = arr[0] - mu
            for i in range(1, n):
                prefix[i] = prefix[i-1] + (arr[i] - mu)
            
            # 注意：我们使用 p[0..n-1]，但经典公式中使用的是 p[0..n-2]
            # 实际上，p[n-1] = 0 总是成立（因为总和为 S，差值总和为 0）
            # 所以我们只排序前 n-1 个值
            if n == 1:
                return 0
            
            # 取 p[0..n-2] 排序
            p = prefix[:-1]  # 前 n-1 个
            p_sorted = sorted(p)
            
            # 中位数
            mid = p_sorted[n // 2 - 1] if n % 2 == 0 else p_sorted[n // 2]
            
            # 计算答案
            ans = sum(abs(x - mid) for x in p)
            
            # 由于操作次数是整数，四舍五入
            # 理论上 ans 应该是整数，但由于浮点数精度，可能接近整数
            return int(round(ans))
        return min_operations_to_nonnegative(balance)




re =Solution().minMoves([-2,4,-2,4,-2,4,-2,4])
print(re)