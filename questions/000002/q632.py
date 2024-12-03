from typing import List, Tuple, Optional
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        c = [0]*n 
        ls = []
        for i,aa in enumerate(nums):
            for a in aa:
                ls.append((a,i))
        ls.sort()
        l = 0 
        cnt = 0
        ret = [ls[0][0], ls[-1][0]]
        for i,(a,idx) in enumerate(ls):
            c[idx] +=1
            if c[idx] ==1:
                cnt +=1
            while cnt == n and c[ls[l][1]] >1:
                c[ls[l][1]] -=1
                l+=1
            if cnt ==n and a- ls[l][0] < ret[1] -ret[0]:
                ret = [ls[l][0],a]
        return ret
    
re =Solution().smallestRange(nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
print(re)