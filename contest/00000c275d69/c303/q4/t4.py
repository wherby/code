

from collections import defaultdict
from email.policy import default


class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt =[0]
        nums= list(set(nums))
        dic =defaultdict(int)
        for a in nums:
            acc=0 
            for i in range(32):
                if a&(1<<i):
                    acc +=1
            dic[acc]+=1
        ret =0
        for a in nums:
            acc=0 
            for i in range(32):
                if a&(1<<i):
                    acc +=1
            res = k -acc
            for i in range(res,32):
                ret +=dic[i]
        return ret
            
            



re =Solution().countExcellentPairs(nums = [1,2,3,1], k = 3)
print(re)