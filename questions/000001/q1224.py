from collections import defaultdict,deque
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 1
        dic = defaultdict(int)
        dic2 = defaultdict(set)
        for i,a in enumerate(nums):
            k = dic[a]
            if k != 0 :
                dic2[k].remove(a)
                if len(dic2[k]) ==0:
                    del dic2[k]
            dic[a] +=1
            dic2[dic[a]].add(a)
            if len(dic2) == 1 and len(dic2[list(dic2.keys())[0]])==1:
                mx = max(mx,i+1)
            if len(dic2) == 1 and dic[list(dic2.keys())[0]] ==1:
                mx = max(mx,i+1)
            if len(dic2) ==2:
                keys = list(dic2.keys())
                if max(keys) -min(keys) ==1 and len(dic2[max(keys)]) ==1:
                    mx = max(mx,i+1)
            if len(dic2) ==2:
                keys = list(dic2.keys())
                if min(keys)==1 and len(dic2[min(keys)]) ==1:
                    mx = max(mx,i+1)     
        return mx

re = Solution().maxEqualFreq([1,1])
print(re)
