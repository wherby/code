from collections import defaultdict
from email.policy import default


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic =defaultdict(int)
        for ls in grid:
            tls = list(ls)
            tls = tuple(tls)
            dic[tls] +=1
        cnt =0
        rg = list(zip(*grid))
        for ls in rg:
            ls = list(ls)
            cnt += dic[tuple(ls)]
        return cnt





re =Solution().equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])
print(re)