from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def extractMantra(self, mt: List[str], mantra: str) -> int:
        m,n = len(mt), len(mt[0])
        dic = defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[mt[i][j]].append((i,j))
        for a in mantra:
            if len(dic[a]) ==0:
                return -1 
        mxc = 10**8
        N = len(mantra)
        visit={}
        @cache 
        def dfs(idx,x,y,cst):
            #print(idx,x,y,cst)
            nonlocal mxc
            if idx == N:
                mxc = min(mxc,cst)
                return
            if cst >= mxc:
                return
            if (idx,x,y) in dic and visit[(idx,x,y)] <=cst:
                return
            st = []
            for a,b in dic[mantra[idx]]:
                k = abs(x-a) + abs(y-b)
                heapq.heappush(st,(k,a,b))
            while st:
                k,a,b = heapq.heappop(st)
                visit[(idx,a,b)] = k+cst+1
                dfs(idx+1,a,b,k+cst+1)
        dfs(0,0,0,0)
        return mxc
                 
        


mt=["aaabaaabbbabaabaababaababbaabbbabbabbabaaabbbbaaabaababababaaaababbbbbaaaaabaabaa","aaaaabbaaabbbabbaabbaaabbbabbabbbbaaabbbbaabbbabbbabbbaabbbbabaabbbbabababaabaaab","abaaababaaaaaaababbbbbbaaaabbbbbabbbabaaaaaabbbbaababbaaaabbbbbabababbbbaaaaabaab","babbababaabaabbbabbababababbabaabaabbabbbababbabbbbbbbaababaabbabbabababbaabaabbb","babbabbbaabaababbabaaaaaababababbabaabababbbbaaabbbbabbbbbbabbabbbbbaaabaabaaaabb","baabbababbbbaaaaabaaaabbbaabbbaabbabbabaaaabbaaaaaabbbaaababbaaaababbbaaabbbababa","aabbbabaaaabbbaabbbbaaaaaaabbababbabaaabbaaabbaababaabbbababbbbabaaababbbaaaaaaba","bbbbbabbbbabaaabbbbbbbbababbabbabababaaaaaabaabbaababbaaaabaabbbaaaabbbbbabaaabab","bbaaabaabaaabababaababbaaababbbbaaabbbaababababaaaabbbabbbbbaaabbaabbaaabbbbbaaaa","aabaabbaabbabbbbbbabbbbbbaabbbabbaaabbbaaabaaaaabaabaaabaabaabbababbbbbabbaabaaab","baaabaabaababbabbbbbaabbaaababaaababaababaaaaaabbbbaaabbbabbbabaaaaaaaaaaaaaaaaaa","bbaabaabaaaabaabaabaaaaaababababababbbaaabaabbbbaababbabbabbbababaabbbaabaababbba","ababaaababaabababbaabaabaaabaabaabbaababbabbbbababaaabbaabbbbbabbbaabbaaaabaaabbb","bbaabbababaabaabaaabaababaabbbaabbbbaaaaabbaaaaaabaabbabbaaaababbbaaababaababaaaa","abbababaaaaaaaababaabaabbbbaabaaabbaabaaabaabbaaaaaabaabbabbaabbbaaaaababbabbaabb","bbabbabaabbbaaaabaababababbaaabaaaabbabbabbabbaabbaaaaaabbbbbabbaaaaaaabbbaabbbba","bbbaabbabbbaabbaaaaaaabbbabbbbaabbbaabbabaabaabbabbbababbbabbbabbbbabbababaaaabaa","aabbaabbbaaaabababaababbaabbaaabbbbaabaababbaaabbbbababbbaababaaabbbabbaabaaabaaa","aabbaabaabaaaaabaabbbbaaabbabbbbaabbbabbaabbabaaabaaabbbbaaabbbbbabaaabababbaabab","babbaababbabbbbbbabbbabaaabbaaabaabababbaaaabbbabaaaabaabaabbababaabbabaaabaabaaa","bababaaaaababaabbaaaabbaaaabaabbbbabbababbaaababbbaababbbbbbbabaabbbabbbaabababba","aaababaababaabbbabbaaabbbabbbbabbbbbbaaaaababbaaabaaababbbaababababaabbaabbbbaaba","bababbaabababbbaaabaaaabbbabbbbbabaaababaaabbbababbaabaaababbaabbbbbbabababbabbba","abbabbbaabbabbbbbbabababaaaabaaababbaabbbbaaabbbabbbabbaaaaababbbaaabbabbbabbaaaa","babaaaaaaaaaaabaaabaaaabababababaaaaabbbbbbabbaababbbaabbaabbbababaaababbabbbbaab","bbabbbabbbaabaaabbbabbaababbbbababbbaabbababbabaaabbbabbabbbbbaabbabbaaaabbaabaaa","babaaabaaaababababbaabaabbbaabaaabbbbabaaabbababbaaaaabaabbbbbbbbabbbababbaababab","babbbbbaabbbbbbabbababbabbbbaabbabaababababbabbbbaaaaaabaabbababbbabbbbbaabaabbaa","bbabbbbabaaaaababbabaabbabbbaabbababbabaabababababbaababbabaaabbaaabaababbbbabbab","bbabababbabaaaabbabaabbbabbbaabbbaabbbaabbbbbbabaaabbbaabaabaaaaabababababaaaaaaa","abbbabababbabababbaaabbbbbaabbaaabbbbbaabbaaaaabbbbababbababaabaaaabbaababaaaaaaa","baabbaaabbbbaaabaabaabbaabbbbaaaaaababbbbabbaabaabbbaabbabbaaababbbbbbaabbbabbaba","baaabbbbbababaabababaaabbbbaaabaababbbbbbbbbabbbbbaaababaaaabbbbaabbaabaababbbbbb","bbaababbbabbbbaababaabbbaaabababbabaaaabbaabbbbbbaaabbbabbbbabbaabababbbbabbbbbba","bababaaaabaaaaabbbbbabababbbaabababaaaabbbbabbbbbbabaaabbaaaabbabbabaaaaababaaaab","bbbaaababbabbbbbabaaabbaaaabbbbbbbabaaaaabaaaabbbbbbaabbbaababbbaababaabaaaababaa","abbabaabbbabbbaaabbbbbbababbabaabbaabababababaabbaabbabaaaaaabaaaabbaaaababaabbba","aababaaabbbbbbbbbbbaaabaabaaabbbaaaabaaabaabaabbbaabbbaababaababababaabbababaabaa","abbabbaaaabbaabbbababbbbbbaaabbbaaaaaaaababbaabbaabbababbbaabbbbbbbabaabbbaaababb","aababaaaababbaaaaaaababaabbabbaaaaababaabbabbaaaaabbbaabbaabbaabbbbbbaaaabbbbabab","bbbaaababaaabbbaaabbbbabaaabbabbaabbbbbaabababbbaababbbbaaaabbbabbbbbaaabbababbba","babbbaabbbaabbbbbaaababbbaababbbababaabaaababbaaaababaaabbbaaaaaabbabaaabaabaaaab","abbbbababaababbbbbbbbababababbaaaaabbaabbababaabaaabaaaabbbabbbaabbaaababaabaaaba","aabbbaaaaababbbaaaaaabaaababbbabaabbabbaababbbabaaaaaaaaabbabbbabaabbbabbbbbbabbb","baaaabababbaabbbaabbbababaaabababbbaabaabbaabbaabbbbababbababbbaaaaababbbbbaaabaa","babbaabababaaabbbaaaaaabbbabbabbbbaaaabbaaaaabbbbababaaabbbabbaababababbaaaababaa","bbaaaabbabbbaabbbaaabaaabaababbbbbbabbbbaaaabbbbbabaaaaabbabbababbbabbabbaabbaaab","aabbbaabbabbabababbbabbbbbabbaabbbbababbbabaaaaababababaaaabbbbaabaaaababbababbbb","bbabbbabbaaabaaaabababbaabaabaaaabbbbaaaaabbaabaabbbbaaaaaabbbbbaaaabbbaabaabbabb","bbbaaaabbbbbbabbbbbbaaabaaaaabbabaababbabbbbabaabbabaabaaababbbabababbbaaaababaaa","bbaabbaababbaaabbbbaabbbaabaababbabbbaaababbbababaaaabbaababaababbbababbababaaaab","abaaaaaaababaaabbbaaababaabbbbbbbabbbbbaababbbbabbbbaabaaaaabaaaabbaaababbbabbaba","baaaaababbbbbbabbbbaaababaaabbababaaabbbbbbbbabbbabbbbaaaaaaaabbbbbaabbabaaaabbbb","abaaaabbbbabababbaabaababbabbababbbabababbabbbabbbbbaaaaaababbabbabaabbababaababb","aabbabbabbbabaabbbaabbbaaaabbabaababbbaaabaababbaababbaaabaabaaabbbaaabbbaabbabba","bbaabbaababbababababaabbabbbbbbabaaababbaababaabbaaabababbbbabaaaaabaabbabbaaaabb","bbbababbaaaaabbaabbbaaaaaaaabaaababaaaaaaabaaabaabaabbaabaabbbbbabbbababbabbaabbb","abaaaabaaabaabababbababbbbbaabbbaaabbbababbbaabaabbababbaaabbbbaaaaabbababbbababb","aaababababaababbbaaaaaaababbabaaaaabbabbabababababaabbbbabbbbaaababaabaababbababb","abbabbbabababaabaabbbbaaaaababaababbabbbbabbbbbababaababbaaaabaabbababaaaabbaaabb","aaaaababbaaaaabaaabbabaaabbbabbaaaabaabbabbababbbaaaabbaaababbbabbabbabaabbbaaaba","aaaaaaabbbaabbbabbbabbbaaabbabbbabaabbbaaabababbbaaaabaababbabbaabbbbaaabbbbbbbba","abaaabaabbbaabbbaabbaababbaabbaaabaababbbaababbabaabaabbabaabbbbbbabbaaaabbbbbbab","aaababaabababbaabbbaababbaabaabbaabababbabbbaabbababaaabaaababbaabbaaaababababaab","abbbbbaaababababbaabababbbbbbaabaabbbabbbbaaaaaaaaaababbbabaaaaababbaaababbbbbaba","babbbbabaabaabbaabababbbababbabbbabaabababbbbaabaabbbababbbbabbbbbabbbbabbbbaaaba","ababbabbbabaaabaabababbbaabaabababbbbbaabbbaaabbaabaaaabbbababbbbabbbbbabaaabbbab","babaaaababbaabbabbaaabbbaababbbabbbbaababbbabaabaaabbaabaabababbbababaababbbaaaab","bbbbabbaaababaaababbabaababbabaaaaaabaabbbabbaaabbbbbbabbbaabbababaaababaabababaa","babbaabbbbbaababbabbbabbbaaaabaababaaaaabababaabbbbaaaaaaaaabbbaaabaabbbabbababba","aaaabbaabaaabbbaabbbabaaabaaaabaababbaabbabaaabbabbaabbababbababbbbbbaaabaabababb","abbbababbaaabbaaabaaabaabbbbbbaabbbaabbabbbabbbbaaaabbbabbbbaaabbabbbaaabababaabb","bbbbbbaaaaababbabbababbbaabbbbbbaaabaaaababaababbbaaaabbabbbabbbbbbbbbbaaaaababab","baaabbbabaabaababbabaabababbaabaaabaaaaaaaabbbaabbaabbbaaaabbaaaaaabababbbaabaaab","bbabbbaaaaaaaabbaabababaaaabbbbbbbaaabbbaabbaabbabbbaaabbbbababbaabbbaaaaaaaabbba","ababbaaaaaaaaaaabaabbaabaaababaaaaababbbabbbbaaaaababbabbbaabaabbbbbaababaabbbbaa","bbaabababaaabbababbbaaabaaabbbaaaaababbbbababaaabaaaabbabbbaabbbbbabaaabaabaaabaa","ababbabbbabbabaabaabbabababbabbbabbabaaaaaababbabbbaababbabaaabaaaabaabbbababbbaa","bbbbbabbabaaaabbaaabbbabababbaaabbababaaaabaaabaabbababaaabbbbabbbabbbbabbbbaabaa","bbbbbbabaabbbaaaaabaaaaababbabbabababaaaabaaabbbbbbaababbaabbbbabaabbbbbaaabbbabb","bbbaaaabbbbabbaaaaaaabbbbabaaabbabaaaaabbbaabbbbaaabaabbbbbbababbabbbaaabbaabaabb","abaaababaaaabbbbabbabababaabbbaabbbabaabbbaabbbaabaabaaaabbabaaabaabaababababaaba","bbbabbbbabaababaaabaabbbaaababaaabaababaaaaaabbbaaabaaaababbbababaabbbbabbabbabaa","aabaababbaaabaaabaaaabbabbbbbbbbbbbbabaabaaaaaaabbababaabbbabbaaaaabaaabbaaabbabb","baabbbaaababaaaaabababababbaaabaaaaabbbabaababaaabbabbabbaaaaaabaabbabbbbabbbaaab","bbabbbaaabbbbaaabaabbaabbabaabbbbbaaabbabbabbaabbbaaaaaabbaabababbbbbaaabbbbaabaa","ababbbbbabbaaaaabbaabbbaabababaabbaaabaabaabaabbaaabbababbbabbbbbbbbaaaababaabaab","aaababaababbbaaaabbabbbabbaaabaaabaaabaaaababaabaaaaaaaaabaabaabaaabbababaaaaabba","abbbabbabbabbabaabababbababaabaabbbabbaabbbbabaaabaaaaaabbaabbbbaabaababbabbbaaaa","aabbaaaaaabaababbabaaaaaaaaabbababbbabaaaaabaabaabaababaabaaabaabababbabaaaaabbaa","bbbbabbbabbaaabbaaaabbabababaabaabbaaababbaabaabbbabababaaabaababbabbaaabaaaaaaaa","abbbaabbaaaabaaaabaaaaaaaaababaaaabbabbbaabaabababbaabaaaaaaababbaabbabbbaaabbabb","bbbbaabbbaaaaaabaaabaababababbabbaabababaabbbbbbabaabbbbabaabaababbbaaababbbabbaa","abbabbbabbaabbaabbbbaaabbaaabbaabbbbbbbbaabbaabbbaaabbaabbbabbabaaababababababaab","bababbabbbaaaaaaaaabaaababababababbbbaaaaaaabaabaaabbbaaaaabbbaabbababaaabaabbaab","bbbbaabbbbbabbaabaaaabbbaabbabaaaabababbababbbbabbbbbbabaabbaabaaaabbabbaabbbaaba","ababaaabbabababbabbbbbabbaabaaababbbbaaabbabbbbabbaababbbbbaaaabbabbbbaaaabaabbba","aaaaababaabbabbaababbbaaababaabaaabbbbbaabaaababaabababbbbbbaabbaaabbaabababaabaa"]
mantra= "aababbbabaabbabaabaaaabaabbbaabbbaababaabbaabaabbbabababbbbbaaabbaabbbbaaabbaaabba"

re =Solution().extractMantra(mt , mantra)
print(re)