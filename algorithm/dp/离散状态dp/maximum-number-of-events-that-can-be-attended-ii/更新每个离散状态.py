# 处理离散状态
# 需要把离散的状态连续遍历，对每个连续的状态处理相邻DP和状态转移DP
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key= lambda x : x[1])
        tls = set([0])
        rdic = defaultdict(list)
        for a,b,c in events:
            tls.add(a)
            tls.add(b)
            rdic[b].append((a,b,c))
        tls = list(tls)
        tls.sort()
        n = len (tls)
        dp = [[0]*(n+1) for _ in range(k+1)]
        mxl = [0]*(k+1)
        for idx in range(1,n):
            for k1 in range(k,0,-1):
                dp[k1][idx] = max(dp[k1][idx],mxl[k1])
            for a,b,c in rdic[tls[idx]]:
                bidx = bisect_left(tls,b)
                aidx = bisect_left(tls,a)
                for k1 in range(k,0,-1):
                    dp[k1][bidx] = max(mxl[k1], dp[k1-1][aidx-1] + c)
                    mxl[k1] = max(mxl[k1],dp[k1][bidx] )
        return max([max(a) for a in dp])


re = Solution().maxValue([[41,54,68],[28,84,88],[35,44,51],[10,64,36],[81,86,25],[6,51,80],[17,99,35],[8,86,22],[82,89,60],[61,73,96],[50,52,28]],11)
print(re)