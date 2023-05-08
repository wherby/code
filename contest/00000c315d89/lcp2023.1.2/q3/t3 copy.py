# https://leetcode.cn/contest/season/2023-spring/ranking/team/
# https://leetcode.cn/contest/season/2023-spring/problems/kjpLFZ/

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
        st = [(0,0,0,0)]
        visit = {}
        N = len(mantra)
        ls  =[10**10]*(N+1)
        ls[0] =0
        stDic = {}
        s = set(mantra)
        sL  = len(s)
        vss = defaultdict(SortedList)
        while st:
            cst,x,y,idx = heapq.heappop(st)
            ls[idx] = min(ls[idx] ,cst)
            if (x,y,idx) in visit: continue
            visit[(x,y,idx)] =cst 
            if len(vss[(x,y)]) and vss[(x,y)][-1]>=idx:continue
            vss[(x,y)].add(idx)
            
            #if cst > ls[idx] + sL*2:continue
            print(cst,x,y,idx)
            if idx == N:
                return cst +N
            #if (x,y,idx) in visit: continue
            for a,b in dic[mantra[idx]]:
                k = abs(x-a) + abs(y-b)
                if (a,b,idx +1) in visit: continue
                if (a,b,idx +1) in stDic and cst + k >=stDic[(a,b,idx+1)]:
                    continue
                stDic[(a,b,idx+1)] = cst+k+1 if (a,b,idx+1) not in stDic else min(cst+k+1,stDic[(a,b,idx+1)])
                #if cst+k+1 > ls[idx+1]+sL*2:continue
                heapq.heappush(st,(cst + k  ,a,b,idx+1)) 
                #visit[(a,b,idx+1)] =cst + k + 1
        
        
                 
        


mt=["aaabaaabbbabaabaababaababbaabbbabbabbabaaabbbbaaabaababababaaaababbbbbaaaaabaabaa","aaaaabbaaabbbabbaabbaaabbbabbabbbbaaabbbbaabbbabbbabbbaabbbbabaabbbbabababaabaaab","abaaababaaaaaaababbbbbbaaaabbbbbabbbabaaaaaabbbbaababbaaaabbbbbabababbbbaaaaabaab","babbababaabaabbbabbababababbabaabaabbabbbababbabbbbbbbaababaabbabbabababbaabaabbb","babbabbbaabaababbabaaaaaababababbabaabababbbbaaabbbbabbbbbbabbabbbbbaaabaabaaaabb","baabbababbbbaaaaabaaaabbbaabbbaabbabbabaaaabbaaaaaabbbaaababbaaaababbbaaabbbababa","aabbbabaaaabbbaabbbbaaaaaaabbababbabaaabbaaabbaababaabbbababbbbabaaababbbaaaaaaba","bbbbbabbbbabaaabbbbbbbbababbabbabababaaaaaabaabbaababbaaaabaabbbaaaabbbbbabaaabab","bbaaabaabaaabababaababbaaababbbbaaabbbaababababaaaabbbabbbbbaaabbaabbaaabbbbbaaaa","aabaabbaabbabbbbbbabbbbbbaabbbabbaaabbbaaabaaaaabaabaaabaabaabbababbbbbabbaabaaab","baaabaabaababbabbbbbaabbaaababaaababaababaaaaaabbbbaaabbbabbbabaaaaaaaaaaaaaaaaaa","bbaabaabaaaabaabaabaaaaaababababababbbaaabaabbbbaababbabbabbbababaabbbaabaababbba","ababaaababaabababbaabaabaaabaabaabbaababbabbbbababaaabbaabbbbbabbbaabbaaaabaaabbb","bbaabbababaabaabaaabaababaabbbaabbbbaaaaabbaaaaaabaabbabbaaaababbbaaababaababaaaa","abbababaaaaaaaababaabaabbbbaabaaabbaabaaabaabbaaaaaabaabbabbaabbbaaaaababbabbaabb","bbabbabaabbbaaaabaababababbaaabaaaabbabbabbabbaabbaaaaaabbbbbabbaaaaaaabbbaabbbba","bbbaabbabbbaabbaaaaaaabbbabbbbaabbbaabbabaabaabbabbbababbbabbbabbbbabbababaaaabaa","aabbaabbbaaaabababaababbaabbaaabbbbaabaababbaaabbbbababbbaababaaabbbabbaabaaabaaa","aabbaabaabaaaaabaabbbbaaabbabbbbaabbbabbaabbabaaabaaabbbbaaabbbbbabaaabababbaabab","babbaababbabbbbbbabbbabaaabbaaabaabababbaaaabbbabaaaabaabaabbababaabbabaaabaabaaa","bababaaaaababaabbaaaabbaaaabaabbbbabbababbaaababbbaababbbbbbbabaabbbabbbaabababba","aaababaababaabbbabbaaabbbabbbbabbbbbbaaaaababbaaabaaababbbaababababaabbaabbbbaaba","bababbaabababbbaaabaaaabbbabbbbbabaaababaaabbbababbaabaaababbaabbbbbbabababbabbba","abbabbbaabbabbbbbbabababaaaabaaababbaabbbbaaabbbabbbabbaaaaababbbaaabbabbbabbaaaa","babaaaaaaaaaaabaaabaaaabababababaaaaabbbbbbabbaababbbaabbaabbbababaaababbabbbbaab","bbabbbabbbaabaaabbbabbaababbbbababbbaabbababbabaaabbbabbabbbbbaabbabbaaaabbaabaaa","babaaabaaaababababbaabaabbbaabaaabbbbabaaabbababbaaaaabaabbbbbbbbabbbababbaababab","babbbbbaabbbbbbabbababbabbbbaabbabaababababbabbbbaaaaaabaabbababbbabbbbbaabaabbaa","bbabbbbabaaaaababbabaabbabbbaabbababbabaabababababbaababbabaaabbaaabaababbbbabbab","bbabababbabaaaabbabaabbbabbbaabbbaabbbaabbbbbbabaaabbbaabaabaaaaabababababaaaaaaa","abbbabababbabababbaaabbbbbaabbaaabbbbbaabbaaaaabbbbababbababaabaaaabbaababaaaaaaa","baabbaaabbbbaaabaabaabbaabbbbaaaaaababbbbabbaabaabbbaabbabbaaababbbbbbaabbbabbaba","baaabbbbbababaabababaaabbbbaaabaababbbbbbbbbabbbbbaaababaaaabbbbaabbaabaababbbbbb","bbaababbbabbbbaababaabbbaaabababbabaaaabbaabbbbbbaaabbbabbbbabbaabababbbbabbbbbba","bababaaaabaaaaabbbbbabababbbaabababaaaabbbbabbbbbbabaaabbaaaabbabbabaaaaababaaaab","bbbaaababbabbbbbabaaabbaaaabbbbbbbabaaaaabaaaabbbbbbaabbbaababbbaababaabaaaababaa","abbabaabbbabbbaaabbbbbbababbabaabbaabababababaabbaabbabaaaaaabaaaabbaaaababaabbba","aababaaabbbbbbbbbbbaaabaabaaabbbaaaabaaabaabaabbbaabbbaababaababababaabbababaabaa","abbabbaaaabbaabbbababbbbbbaaabbbaaaaaaaababbaabbaabbababbbaabbbbbbbabaabbbaaababb","aababaaaababbaaaaaaababaabbabbaaaaababaabbabbaaaaabbbaabbaabbaabbbbbbaaaabbbbabab","bbbaaababaaabbbaaabbbbabaaabbabbaabbbbbaabababbbaababbbbaaaabbbabbbbbaaabbababbba","babbbaabbbaabbbbbaaababbbaababbbababaabaaababbaaaababaaabbbaaaaaabbabaaabaabaaaab","abbbbababaababbbbbbbbababababbaaaaabbaabbababaabaaabaaaabbbabbbaabbaaababaabaaaba","aabbbaaaaababbbaaaaaabaaababbbabaabbabbaababbbabaaaaaaaaabbabbbabaabbbabbbbbbabbb","baaaabababbaabbbaabbbababaaabababbbaabaabbaabbaabbbbababbababbbaaaaababbbbbaaabaa","babbaabababaaabbbaaaaaabbbabbabbbbaaaabbaaaaabbbbababaaabbbabbaababababbaaaababaa","bbaaaabbabbbaabbbaaabaaabaababbbbbbabbbbaaaabbbbbabaaaaabbabbababbbabbabbaabbaaab","aabbbaabbabbabababbbabbbbbabbaabbbbababbbabaaaaababababaaaabbbbaabaaaababbababbbb","bbabbbabbaaabaaaabababbaabaabaaaabbbbaaaaabbaabaabbbbaaaaaabbbbbaaaabbbaabaabbabb","bbbaaaabbbbbbabbbbbbaaabaaaaabbabaababbabbbbabaabbabaabaaababbbabababbbaaaababaaa","bbaabbaababbaaabbbbaabbbaabaababbabbbaaababbbababaaaabbaababaababbbababbababaaaab","abaaaaaaababaaabbbaaababaabbbbbbbabbbbbaababbbbabbbbaabaaaaabaaaabbaaababbbabbaba","baaaaababbbbbbabbbbaaababaaabbababaaabbbbbbbbabbbabbbbaaaaaaaabbbbbaabbabaaaabbbb","abaaaabbbbabababbaabaababbabbababbbabababbabbbabbbbbaaaaaababbabbabaabbababaababb","aabbabbabbbabaabbbaabbbaaaabbabaababbbaaabaababbaababbaaabaabaaabbbaaabbbaabbabba","bbaabbaababbababababaabbabbbbbbabaaababbaababaabbaaabababbbbabaaaaabaabbabbaaaabb","bbbababbaaaaabbaabbbaaaaaaaabaaababaaaaaaabaaabaabaabbaabaabbbbbabbbababbabbaabbb","abaaaabaaabaabababbababbbbbaabbbaaabbbababbbaabaabbababbaaabbbbaaaaabbababbbababb","aaababababaababbbaaaaaaababbabaaaaabbabbabababababaabbbbabbbbaaababaabaababbababb","abbabbbabababaabaabbbbaaaaababaababbabbbbabbbbbababaababbaaaabaabbababaaaabbaaabb","aaaaababbaaaaabaaabbabaaabbbabbaaaabaabbabbababbbaaaabbaaababbbabbabbabaabbbaaaba","aaaaaaabbbaabbbabbbabbbaaabbabbbabaabbbaaabababbbaaaabaababbabbaabbbbaaabbbbbbbba","abaaabaabbbaabbbaabbaababbaabbaaabaababbbaababbabaabaabbabaabbbbbbabbaaaabbbbbbab","aaababaabababbaabbbaababbaabaabbaabababbabbbaabbababaaabaaababbaabbaaaababababaab","abbbbbaaababababbaabababbbbbbaabaabbbabbbbaaaaaaaaaababbbabaaaaababbaaababbbbbaba","babbbbabaabaabbaabababbbababbabbbabaabababbbbaabaabbbababbbbabbbbbabbbbabbbbaaaba","ababbabbbabaaabaabababbbaabaabababbbbbaabbbaaabbaabaaaabbbababbbbabbbbbabaaabbbab","babaaaababbaabbabbaaabbbaababbbabbbbaababbbabaabaaabbaabaabababbbababaababbbaaaab","bbbbabbaaababaaababbabaababbabaaaaaabaabbbabbaaabbbbbbabbbaabbababaaababaabababaa","babbaabbbbbaababbabbbabbbaaaabaababaaaaabababaabbbbaaaaaaaaabbbaaabaabbbabbababba","aaaabbaabaaabbbaabbbabaaabaaaabaababbaabbabaaabbabbaabbababbababbbbbbaaabaabababb","abbbababbaaabbaaabaaabaabbbbbbaabbbaabbabbbabbbbaaaabbbabbbbaaabbabbbaaabababaabb","bbbbbbaaaaababbabbababbbaabbbbbbaaabaaaababaababbbaaaabbabbbabbbbbbbbbbaaaaababab","baaabbbabaabaababbabaabababbaabaaabaaaaaaaabbbaabbaabbbaaaabbaaaaaabababbbaabaaab","bbabbbaaaaaaaabbaabababaaaabbbbbbbaaabbbaabbaabbabbbaaabbbbababbaabbbaaaaaaaabbba","ababbaaaaaaaaaaabaabbaabaaababaaaaababbbabbbbaaaaababbabbbaabaabbbbbaababaabbbbaa","bbaabababaaabbababbbaaabaaabbbaaaaababbbbababaaabaaaabbabbbaabbbbbabaaabaabaaabaa","ababbabbbabbabaabaabbabababbabbbabbabaaaaaababbabbbaababbabaaabaaaabaabbbababbbaa","bbbbbabbabaaaabbaaabbbabababbaaabbababaaaabaaabaabbababaaabbbbabbbabbbbabbbbaabaa","bbbbbbabaabbbaaaaabaaaaababbabbabababaaaabaaabbbbbbaababbaabbbbabaabbbbbaaabbbabb","bbbaaaabbbbabbaaaaaaabbbbabaaabbabaaaaabbbaabbbbaaabaabbbbbbababbabbbaaabbaabaabb","abaaababaaaabbbbabbabababaabbbaabbbabaabbbaabbbaabaabaaaabbabaaabaabaababababaaba","bbbabbbbabaababaaabaabbbaaababaaabaababaaaaaabbbaaabaaaababbbababaabbbbabbabbabaa","aabaababbaaabaaabaaaabbabbbbbbbbbbbbabaabaaaaaaabbababaabbbabbaaaaabaaabbaaabbabb","baabbbaaababaaaaabababababbaaabaaaaabbbabaababaaabbabbabbaaaaaabaabbabbbbabbbaaab","bbabbbaaabbbbaaabaabbaabbabaabbbbbaaabbabbabbaabbbaaaaaabbaabababbbbbaaabbbbaabaa","ababbbbbabbaaaaabbaabbbaabababaabbaaabaabaabaabbaaabbababbbabbbbbbbbaaaababaabaab","aaababaababbbaaaabbabbbabbaaabaaabaaabaaaababaabaaaaaaaaabaabaabaaabbababaaaaabba","abbbabbabbabbabaabababbababaabaabbbabbaabbbbabaaabaaaaaabbaabbbbaabaababbabbbaaaa","aabbaaaaaabaababbabaaaaaaaaabbababbbabaaaaabaabaabaababaabaaabaabababbabaaaaabbaa","bbbbabbbabbaaabbaaaabbabababaabaabbaaababbaabaabbbabababaaabaababbabbaaabaaaaaaaa","abbbaabbaaaabaaaabaaaaaaaaababaaaabbabbbaabaabababbaabaaaaaaababbaabbabbbaaabbabb","bbbbaabbbaaaaaabaaabaababababbabbaabababaabbbbbbabaabbbbabaabaababbbaaababbbabbaa","abbabbbabbaabbaabbbbaaabbaaabbaabbbbbbbbaabbaabbbaaabbaabbbabbabaaababababababaab","bababbabbbaaaaaaaaabaaababababababbbbaaaaaaabaabaaabbbaaaaabbbaabbababaaabaabbaab","bbbbaabbbbbabbaabaaaabbbaabbabaaaabababbababbbbabbbbbbabaabbaabaaaabbabbaabbbaaba","ababaaabbabababbabbbbbabbaabaaababbbbaaabbabbbbabbaababbbbbaaaabbabbbbaaaabaabbba","aaaaababaabbabbaababbbaaababaabaaabbbbbaabaaababaabababbbbbbaabbaaabbaabababaabaa"]
mantra= "aababbbabaabbabaabaaaabaabbbaabbbaababaabbaabaabbbabababbbbbaaabbaabbbbaaabbaaabba"
#mt=["aaknqmyqifgv","dlwayfyomlta","dgzxmkwwvjru","yxwaxfsqrfvj","pbgwirqrgunu","aafaxkjjolpi","lbinkhqnxabr","ikuwecqhmmzd","tzraxzeeaxuk","lxutzbqlweye","daydrducohyc","nmahtpcvcgcy"]
#mantra="kujnpuqpyzoeekgccnzhtfrrlhu"
re =Solution().extractMantra(mt , mantra)
#re =Solution().extractMantra(mt = ["sss","epdd"], mantra = "speed")
print(re)