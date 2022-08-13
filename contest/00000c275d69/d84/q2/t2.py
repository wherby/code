from collections import defaultdict


class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for i,a in enumerate(nums):
            dic[a-i] +=1
        n = len(nums)
        cnt =0
        for k,v in dic.items():
            cnt += v *(n-v)
        return cnt//2





re =Solution().countBadPairs([4,1,3,3])
print(re)