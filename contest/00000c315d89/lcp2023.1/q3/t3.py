from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def fieldOfGreatestBlessing(self, fs: List[List[int]]) -> int:
        cands = []
        fs = [(a,b,c/2 ) for a,b,c in fs ]
        for a,b,c in fs:
            cands.append((a-c,b-c))
            cands.append((a-c,b+c))
            cands.append((a+c,b-c))
            cands.append((a+c,b+c))
        mx = 0
        for x,y in cands:
            acc =0
            for a,b,c in fs:
                if abs(x-a) <=c+0.001 and abs(y-b) <=c+0.001:
                    acc +=1
            if mx < acc:
                mx = acc
        return mx



ls = [[565,34,242],[299,628,870],[724,673,221],[128,267,917],[561,488,696],[341,71,604],[835,92,846],[945,696,973],[554,776,430],[209,134,594],[987,898,282],[819,154,462],[618,946,505],[561,40,677],[602,863,657],[295,83,718],[456,920,939],[94,717,813],[611,946,366],[818,850,85],[395,554,333],[325,700,628],[590,401,119],[248,858,499],[298,723,602],[189,538,646],[194,283,344],[842,535,866],[192,832,195]]
re =Solution().fieldOfGreatestBlessing(ls)
print(re)