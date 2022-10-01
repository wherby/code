
from math import inf
import heapq


            
class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        seens =[inf]*n
        st =[]
        st.append([0,0])
        st.append([0,firstPerson])
        g = [[] for _ in range(n)]
        for a,b,t in meetings:
            g[a].append([b,t])
            g[b].append([a,t])
        visit = [0]*n
        while st:
            t,a = heapq.heappop(st)
            if visit[a] ==0:
                visit[a] =1
                seens[a] = t 
                for b,t2 in g[a]:
                    if visit[b] ==0 and t2 >=t :
                        heapq.heappush(st,[t2,b])
        res =[]
        for i in range(n):
            if seens[i] != inf:
                res.append(i)
        
        return res
    
re =Solution().findAllPeople(6,[[0,2,1],[1,3,1],[4,5,1]],1)
print(re)