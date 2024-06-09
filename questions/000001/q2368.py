from typing import List, Tuple, Optional
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        sm = 0
        ls =[]
        for a in nums:
            if a >0:
                sm += a 
                ls.append(a)
            else:
                ls.append(-a)
        cand = [0]
        ls.sort()
        for a in ls:
            tmp =[]
            if len(cand) ==k and a >=cand[-1]:
                continue
            for b in cand:
                tmp.append(a+b)
            tmp.extend(cand)
            tmp.sort()
            tmp = tmp[:k]
            cand = tmp
        return sm -tmp[-1]

re = Solution().kSum(nums = [2,4,-2], k = 5)
print(re)
        