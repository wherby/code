class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        n =len(s)
        cnt =1
        mod = 10**9+7
        for i in range(1,n):
            if s[i] == s[i-1]:
                cnt +=1
            else:
                res +=cnt * (cnt +1) //2
                cnt =1
        res +=cnt * (cnt +1) //2
        return res %mod

re = Solution().countHomogenous("abbcccaa")
print(re)