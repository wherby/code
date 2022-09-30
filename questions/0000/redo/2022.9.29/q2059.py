class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        dp = [10**10] *1001
        dp[start] =0
        visit={}
        visit[start]=0
        cand = [start]
        while cand:
            tmp = set()
            for a in cand:
                for b in nums:
                    if 0<=a+b<=1000 and a+b not in visit:
                        dp[a+b] = min(dp[a+b], dp[a] +1)
                        tmp.add(a+b)
                    if 0<=a-b<=1000 and a-b not in visit:
                        dp[a-b] = min(dp[a-b], dp[a] +1)
                        tmp.add(a-b)
                    if 0<=a^b<=1000 and a^b not in visit:
                        dp[a^b] = min(dp[a^b], dp[a] +1)
                        tmp.add(a^b)
            for a in tmp:
                visit[a] =1
            cand = tmp
            #print(cand)
        #print(cand,dp)
         
        ret = 10**10
        if 0<=goal<=1000:
            ret = min(ret,dp[goal])
        for a in nums:
            if 0<=goal + a <=1000:
                ret = min(ret , dp[goal +a] +1)
            if 0<= goal-a <=1000:
                ret = min(ret,dp[goal-a] +1)
            if 0<=goal^ a <=1000:
                ret = min(ret,dp[goal ^a] +1)
        #print(dp)
        return ret if ret <10**10 else -1
        

re = Solution().minimumOperations([-574938140,347713845,925500837,-396559946,-39213216,-696511059,-701862040,-547815957,-613314611,814380075,446824702,397447568,709912715,144793599,812441247,-59489753,857299470,360355629,85411951,-439873837,-477453514,-887964831,-914549223,633449658,452658511,657134722,1],827,-547815957)
print(re)