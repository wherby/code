from collections import Counter
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        cnt = 0
        c1 =Counter(tasks)
        for k,v in c1.items():
            if v==1:
                return -1
            cnt += (v+2) //3
        return cnt 
    
re =Solution().minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4])
print(re)