## 用BFS的方式求直径
from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def getDis(edges):
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            def bfs(start):
                dis = [-1] * n
                dis[start] = 0
                q = deque([start])
                while q:
                    u = q.popleft()
                    end = u
                    for v in g[u]:
                        if dis[v] == -1:
                            dis[v] = dis[u] + 1
                            q.append(v)
                return dis,end
            _,p1 = bfs(0)
            dis1,p2 = bfs(p1)
            dis2,_ = bfs(p2)
            return [max(dis1[i],dis2[i]) for i in range(n)]
        dis1 = getDis(edges1)
        dis2 = getDis(edges2)
        return max(max(dis1),max(dis2),min(dis1) + min(dis2) + 1)

#作者：雪景式
#链接：https://leetcode.cn/circle/discuss/IMqrLP/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。