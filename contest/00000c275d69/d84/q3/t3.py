from collections import Counter


class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        acc =0
        dic = {}
        idx = 0
        for a in tasks:
            if a not in dic:
                idx +=1
                dic[a] = idx 
            else:
                t = dic[a]
                idx = max(idx +1, t +space+1)
                dic[a] = idx
        return idx 
            





re =Solution().taskSchedulerII(tasks = [1,2,1,2,3,1], space = 3)
print(re)