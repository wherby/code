import functools
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
       
        n = len(tasks)
        @functools.lru_cache(None) 
        def dfs(mask):
            if mask ==0:
                return (1,0)
            ans =(n+1,n+1)
            for i in range(n):
                if mask & 1<<i:
                    pieces,last = dfs(mask-(1<<i))
                    full = (last + tasks[i]) > sessionTime
                    ans = min(ans,(pieces + full,tasks[i] + (1-full)*last))
            return ans
        return dfs((1<<n)-1)[0]

#re = Solution().minSessions(tasks = [1,2,3], sessionTime = 3)
re = Solution().minSessions([1,1,2,2,2,2,3,3,6,6,6,6],10)
print(re)
