# https://leetcode.cn/problems/maximum-score-of-non-overlapping-intervals/description/
# https://leetcode.cn/problems/maximum-score-of-non-overlapping-intervals/solutions/3039058/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-wmuy/
from typing import List, Tuple, Optional


from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        invs = [(b,a,c,i) for i,(a,b,c) in enumerate(intervals)]
        invs.sort()
        n = len(invs)
        dp = [[(0,[]) for _ in range(5)] for _ in range(n+1)]
        #print(invs)
        for i,(b,a,c,idx) in enumerate(invs):
            k = bisect_left(invs,(a-1,10**19,),hi=i)
            for j in range(1,5):
                s1,ids = dp[k][j-1]
                dp[i+1][j] = min(dp[i][j],(s1-c,sorted(ids + [idx])))
        #print(dp)
        return dp[-1][4][1]
        




#re =Solution().maximumWeight(intervals =[[8,15,32],[20,21,8],[8,16,29],[7,12,50],[16,25,27],[12,17,2],[8,12,45],[5,10,50]])
re =Solution().maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]])
print(re)