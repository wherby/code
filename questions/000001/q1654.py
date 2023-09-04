from typing import List, Tuple

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        fs = set(forbidden)
        cand =[(0,0,False)]
        def verify(x):
            if x in fs or x <0:
                return False
            return True
        dic={}
        MX =10**10
        while cand:
            res =[]
            for idx,cnt,isB in cand:
                #print(idx,cnt,isB)
                if idx > 6000:continue
                if dic.get((isB,idx),MX) <=cnt:continue 
                dic[(isB,idx)] =cnt 
                if idx == x:
                    return cnt
                if verify(idx +a):
                    res.append([idx+a,cnt+1,False])
                if isB == False and verify(idx-b):
                    res.append([idx-b,cnt+1,True])
            cand = res
        return  -1


re = Solution().minimumJumps([1998],1999,2000,2000)
print(re)