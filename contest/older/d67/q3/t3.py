from collections import defaultdict
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        g = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i ==j : continue
                b1= bombs[i]
                b2 = bombs[j]
                dist = (b1[0]-b2[0]) **2  + (b1[1] - b2[1])**2
                if dist <= (b1[2] **2):
                    g[i].append(j)
        def dfs(i):
            nonlocal cnt
            cnt +=1
            for k in g[i]:
                if visited[k] ==0:
                    visited[k] =1
                    dfs(k)
        cnt =0
        mx =0
        for i in range(n):
            visited = [0]*n
            cnt =0
            visited[i] =1
            dfs(i)
            if cnt >mx:
                mx =cnt
        return mx

re = Solution().maximumDetonation(bombs = [[4,4,3],[4,4,3]])
print(re)
