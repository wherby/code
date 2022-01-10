#@ TimeOut

import functools
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        mx = n
        tasks.sort()
        validState = []
        
        @functools.lru_cache(None) 
        def verify(subSet):
            cnt =0
            for i in range(n):
                if 1<<i & subSet >0:
                    cnt += tasks[i]
            return cnt <= sessionTime
        for i in range(1,1<<n):
            if verify(i):
                validState.append(i)
        #print(validState)
        @functools.lru_cache(None) 
        def dfs(state,cnt):
            nonlocal mx
            if cnt > mx:
                return
            if state ==0:
                mx = min(mx,cnt)
            for va in validState:
                if va &state == va:
                    dfs(state-va, cnt+1)
        dfs((1<<n)-1,0)
        return mx

re = Solution().minSessions([1,1,1,1,1,1,1,1,1,1,1,1,1,1],14)
print(re)