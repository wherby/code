from typing import List, Tuple, Optional

from sortedcontainers import SortedDict,SortedList
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(rowSum),len(colSum)
        m = [[0]*n for _ in range(m)]
        slRow,slCol= SortedList([]),SortedList([])
        for i,a in enumerate(rowSum):
            slRow.add((a,i))
        for i,a in enumerate(colSum):
            slCol.add((a,i))
        while len(slRow) >0 and len(slCol)>0:
            rowLow,idxRow = slRow.pop(0)
            colLow,idxCol = slCol.pop(0)
            if rowLow < colLow:
                m[idxRow][idxCol] = rowLow
                slCol.add((colLow-rowLow,idxCol))
            else:
                m[idxRow][idxCol] = colLow
                slRow.add((rowLow-colLow, idxRow))
        return m





re = Solution().restoreMatrix(rowSum = [3,8], colSum = [4,7])
print(re)