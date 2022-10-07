# https://leetcode.cn/problems/1GxJYY/

from collections import defaultdict


class Solution(object):
    def beautifulBouquet(self, flowers, cnt):
        """
        :type flowers: List[int]
        :type cnt: int
        :rtype: int
        """
        dic =defaultdict(int)
        n = len(flowers)
        flowers= flowers[::-1]
        left = 0
        mls = [0]*n
        for i,a in enumerate(flowers):
            dic[a] +=1
            while dic[a] > cnt :
                mls[left] = i-left
                dic[flowers[left]] -=1
                left +=1
        for i in range(left,n):
            mls[i] = n-i
        mod = 10**9+7
        return sum(mls)%mod
re =Solution().beautifulBouquet(flowers = [1,2,3,2], cnt = 1)
print(re)