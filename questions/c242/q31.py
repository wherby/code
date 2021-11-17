import heapq
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        dp = [-1]* n

        cnt1 =0
        for i in range(n):
            if s[i] =="0":
                dp[i] =0
                cnt1= 0
            else:
                cnt1 +=1
                if cnt1 >= maxJump:
                    return False
        if dp[-1] != 0:
            return False
        q = [n-1]
        while q:
            t = heapq.heappop(q)
            dp[t] = -1
            for i in range(minJump,min(maxJump,t)+1):
                if dp[t-i] ==0:
                    heapq.heappush(q,t-i)
                    if t-i ==0:
                        return True
        return False
