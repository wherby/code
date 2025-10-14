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

class Solution:
    def longestBalanced(self, s: str) -> int:
        pre = [[0]*26]
        for a in s:
            t = ord(a)-ord('a')
            t1 =list(pre[-1])
            t1[t] +=1
            pre.append(t1)
        n = len(s)
        mx = 0
        for i in range(1,n+1):
            t1 = pre[i]
            for j in range(n):
                t2 = pre[j]
                t3 = [a-b for a,b in zip(t1,t2)]
                t3 = [a for a in t3 if a != 0]
                if len(set(t3)) ==1:
                    mx = max(mx,i-j)
        return mx




s ="dedbecdceaccceedeacccacaeaeabadddaabdeaaccecaddcacdddbddeededecdcbecdcdcaeccaedeeadcbabaaabbdcdbbbdbbbddececdabddaedaeabdaaeedbdbdedaedbeaaecadadccadbacedceecdbaecaacceccacabbeadcdacaeecedccbbdaaedebbaabceecddccccbddacaecbedbddeaceacebcbbcabebceceadbbdbdddaaabcbeebaaaabbeeebdbdaababedcbcbbaccabecacebeaecebedeacdeabcbebcacbadbdaaebbcdaddedcebaeabeaedebebddcadebaddbdbbdbebaceaaecaccabacdcedbcabdacaadeabebbdbbbbcebdbaaccabdbebacadcaacbeedabddcbaadbecbcbcacbdaacadeddcedbbadcabebcacdbedbaaddcdeabbadbbcdaaeacabcbaaaddbbeccdbcdaabbecddaeaccabdeacaabbedabbdedadaccbbdebdbeacddbaeeeabbccbbabdccaeaeebdcdebeddbbcceabcabacdcebacddddadabeccbddcbdabbeceeecacaacedadaadabddcaceccdbbecaebbeeadacaddddaadcbebbdcbededdbaabadedbadcccbdcdbbeccceeedabbaaebdecaebedbcccbdddbcdcbadcdcabbcbaeaeabccbbaaadbbdceeccbbaaebeeceeadcdcccebeecdaddebaedeeaddebddeccbeabeccadacbcadeebedbeebbedaaedbbeddccaaabeabbcdababddcaebbecdebdcd"
re =Solution().longestBalanced( s)
print(re)