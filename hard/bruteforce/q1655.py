# TDK Bruteforce 
from collections import Counter 
class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """ 
        nc = Counter(nums)
        ls =list(nc.values())
        n = len(ls)
        dp = [[False]*1024 for _ in range(51)]
        for i in range(n+1):
            dp[i][0] = True
        m = len(quantity)
        dic = {}
        for i in range(2**m):
            cnt =0
            for j in range(m):
                if (1<<j) & i :
                    cnt += quantity[j]
            dic[i] = cnt
        #print(dic,ls)
        for i in range(1,n+1):
            for state in range(1,2**m):
                if dp[i-1][state] == True:
                    dp[i][state] = True
                    continue
                subset = state
                while subset>0:
                    if dp[i-1][state-subset] == False:
                        subset = (subset)-1 &state
                        continue
                    #print(ls[i-1],dic[subset],subset)
                    if ls[i-1] >= dic[subset]:
                        dp[i][state] = True
                        break
                    subset = (subset)-1 &state
        return dp[n][(2**m)-1]



nums=[420,420,420,235,687,420,420,591,759,420,420,420,326,756,420,376,420,989,387,212,420,89,420,420,326,420,420,420,387,387]
q=[1,3,1,4]
re =Solution().canDistribute([1,2,3,3] , [2])
print(re)

