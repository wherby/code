from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
from collections import Counter
class Solution:
    def longestBalanced(self, s: str) -> int:
        mx = 0
        n = len(s)
        for i in range(n):
            c = Counter()
            for j in range(i,n):
                c[s[j]] +=1
                if len(set(c.values())) ==1:
                    mx = max(j-i+1,mx)
        return mx




s ="dedbecdceaccceedeacccacaeaeabadddaabdeaaccecaddcacdddbddeededecdcbecdcdcaeccaedeeadcbabaaabbdcdbbbdbbbddececdabddaedaeabdaaeedbdbdedaedbeaaecadadccadbacedceecdbaecaacceccacabbeadcdacaeecedccbbdaaedebbaabceecddccccbddacaecbedbddeaceacebcbbcabebceceadbbdbdddaaabcbeebaaaabbeeebdbdaababedcbcbbaccabecacebeaecebedeacdeabcbebcacbadbdaaebbcdaddedcebaeabeaedebebddcadebaddbdbbdbebaceaaecaccabacdcedbcabdacaadeabebbdbbbbcebdbaaccabdbebacadcaacbeedabddcbaadbecbcbcacbdaacadeddcedbbadcabebcacdbedbaaddcdeabbadbbcdaaeacabcbaaaddbbeccdbcdaabbecddaeaccabdeacaabbedabbdedadaccbbdebdbeacddbaeeeabbccbbabdccaeaeebdcdebeddbbcceabcabacdcebacddddadabeccbddcbdabbeceeecacaacedadaadabddcaceccdbbecaebbeeadacaddddaadcbebbdcbededdbaabadedbadcccbdcdbbeccceeedabbaaebdecaebedbcccbdddbcdcbadcdcabbcbaeaeabccbbaaadbbdceeccbbaaebeeceeadcdcccebeecdaddebaedeeaddebddeccbeabeccadacbcadeebedbeebbedaaedbbeddccaaabeabbcdababddcaebbecdebdcd"
re =Solution().longestBalanced( s)
print(re)