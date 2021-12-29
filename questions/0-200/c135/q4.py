#https://github.com/wisdompeak/LeetCode/tree/master/Greedy/1040.Moving-Stones-Until-Consecutive-II

from bisect import bisect_right,bisect_left
class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        n = len(stones)
        mx  = stones[-1]-stones[0] +2 - n - min(stones[1]-stones[0],stones[n-1]-stones[n-2])
        #print(mx)
        dic= {}
        for s in stones:
            dic[s] =1
        mn = n
        for i in range(0,n-1):
            k = stones[i] + n-1
            if k >stones[-1]:
                continue
            idx = bisect_left(stones,k)
            if k in dic:
                mn = min(mn,n-(idx-i+1))
            else:
                if idx-i == n-1:
                    mn = min(mn,2)
                else:
                #print(extra,idx,n,i)
                    mn =min(mn, n-(idx-i))
            #print(mn)
        return [mn,mx]

re = Solution().numMovesStonesII([6,5,4,3,10])
print(re)