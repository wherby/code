# using Cache value in dfs to record query result

from typing import List, Tuple, Optional
from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            g[i].append(j)

        @cache
        def dfs(r,s):#查询r->s?
            for q in g[r]:
                if q == s or dfs(q,s):
                    return True
            return False

        return [dfs(i,j) for i,j in queries]

#作者：DL_ykx
#链接：https://leetcode.cn/problems/course-schedule-iv/solutions/2438681/dfsdi-gui-by-kind-chatterjeeuu0-6cey/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。