from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic ={}
        ret =0
        for a in ideas:
            dic[a] = 1
        dic2 = defaultdict(int)
        for a in ideas:
            for b in 'abcdefghijklmnopqrstuvwxyz':
                if b +a[1:] not in dic:
                    ret += dic2[(b,a[0])]
                    dic2[(a[0],b)]+=1
        return ret*2
    
re =Solution().distinctNames(["coffee","donuts","time","toffee"])
print(re)