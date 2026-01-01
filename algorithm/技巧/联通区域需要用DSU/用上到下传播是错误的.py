# https://leetcode.cn/problems/last-day-where-you-can-still-cross/description/?envType=daily-question&envId=2025-12-31



# 联通区域可能有回字型，所以从上到下遍历是错误的
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        m,n = row,col 
        cells =[[a-1,b-1] for a,b in cells]
        def verify(mid):
            dic = defaultdict(set)
            for x,y in cells[mid:]:
                dic[x].add(y)
            cand = list(dic[0])
            for i in range(1,m):
            
                vis={}
                tmp=set()
                while cand:
                    a = cand.pop()
                    if a in vis:
                        continue
                    vis[a] = 1 
                    if a in dic[i]:
                        tmp.add(a)
                        if a-1 >=0  and a-1 in dic[i] and a-1 not in vis:
                            cand.append(a-1)
                        if a+1 < n and a+1 in dic[i] and a+1 not in vis:
                            cand.append(a+1)
                cand = list(tmp)
                print(i,cand,mid)
            return len(cand)>0
        l,r = 0,m*n
        while l<r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid-1
        return l

cells = [[12,6],[3,4],[2,9],[9,4],[9,2],[6,4],[4,4],[8,6],[4,9],[5,6],[7,5],[12,4],[11,8],[3,7],[2,6],[9,8],[3,5],[13,4],[1,3],[10,2],[8,9],[6,6],[11,7],[11,1],[13,9],[12,7],[10,7],[8,2],[1,8],[7,3],[6,5],[2,1],[10,6],[4,8],[4,2],[9,7],[6,2],[3,6],[12,2],[10,3],[10,5],[9,5],[8,8],[8,7],[3,2],[13,6],[3,1],[5,1],[2,7],[8,3],[12,5],[11,2],[6,3],[1,4],[13,3],[4,1],[9,9],[7,7],[4,3],[12,1],[2,2],[7,6],[4,6],[7,9],[7,2],[3,8],[1,6],[11,3],[11,4],[5,9],[13,8],[1,9],[10,1],[9,1],[6,1],[10,9],[12,9],[11,5],[8,1],[13,5],[9,6],[13,2],[6,8],[2,8],[5,3],[3,3],[13,1],[11,9],[9,3],[2,4],[5,2],[8,5],[13,7],[12,8],[5,5],[7,1],[7,4],[2,5],[6,9],[4,7],[5,8],[1,5],[10,8],[8,4],[1,1],[3,9],[1,2],[7,8],[1,7],[6,7],[11,6],[4,5],[5,7],[2,3],[10,4],[5,4],[12,3]]
re =Solution().latestDayToCross(13,9,cells=cells)
print(re,35)