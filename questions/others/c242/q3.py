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
        cnt0=0
        cnt1=0
        for i in range(n):
            if s[i] =="0":
                cnt1=0
                dp[i] =cnt0
                cnt0 +=1
            else:
                cnt0=0
                cnt1 +=1
                if cnt1>= maxJump:
                    return False
        i = n-1
        #print(dp)
        while i >0:
            if dp[i] >= minJump:
                j =i
                while dp[j] >minJump:
                    dp[j] = minJump
                    j -=1
                i = j
            i -=1
        #print(dp)
        if dp[n-1] == -1:
            return False
        q = [n-1]
        jp = 1
        while q:
            t = q.pop(0)

            jp +=1
            for i in range(min(maxJump,t),minJump-1,-1):
                k = t-i
                if dp[k] >=0:
                    dp[k] = jp
                    q.append(k)
                    if k ==0:
                        return True
        #print(dp)
        return dp[0] != 0

s="0111000110"


re = Solution().canReach(s,2,4)
print(re)