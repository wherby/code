class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls=[]
        N= 10**5
        pre= [0]*(N+1)
        mod = 10**9+7
        for i in range(1,N+1):
            pre[i]= pre[i-1] +i 
        
        res = 0
        
        cnt =1
        n = len(s)
        for i in range(1,n):
            if s[i] == s[i-1]:
                cnt +=1
            else:
                ls.append(cnt)
                cnt =1
        ls.append(cnt)
        for x in ls:
            res += pre[x]
        return res %mod

re = Solution().countHomogenous("abbcccaa")
print(re)