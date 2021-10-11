
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        near= [[] for i in range(numCourses+1)]
        for reqeust in prerequisites:
            a = reqeust[0]
            b = reqeust[1]
            near[b].append(a)
        visited = [0] * (numCourses +1)
        def dfs(x):
            visited[x] =2
            for a  in  near[x]:
                if visited[a] == 1 : continue
                if visited[a] == 2 : return False
                if dfs(a) == False : return False
            visited[x] =1
            return True
        for i in range(numCourses +1):
            if visited[i] ==0 :
                r = dfs(i)
                if r == False:
                    return False
        return True
