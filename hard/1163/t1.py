from collections import defaultdict
class Solution:

    def lastSubstring(self, s: str) -> str:
        re =s
        n = len(s)
        def filterOut(indexArry,length):
            res =[]
            dic =defaultdict(list)
            mx = "a"
            for index in indexArry:
                if index + length >= n:
                    continue
                t= s[index + length]
                if t > mx:
                    mx = t
                dic[t].append(index)
            return dic[mx]
        cand = [i for i in range(n)]
        for i in range(n):
            next = filterOut(cand,i)
            #print(next)
            if len(next) == 1:
                return s[next[0]:]
            cand =next
        
re =Solution().lastSubstring("leetcode")
print(re)
        
        