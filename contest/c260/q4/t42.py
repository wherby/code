from collections import defaultdict
import functools
class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        @functools.lru_cache(None)
        def dp(start,end):
            res = {}
            if start == end:
                return {int(s[start])}
            
            for m in range(start+1,end,2):
                for a in dp(start, m-1):
                    for b in dp(m+1,end):
                        #print(a,b)
                        t = a*b if s[m] == "*" else a+b
                        if t <=1000:
                            res[t] =2
                        #print(len(res))
            #print(*res.items())
            return res
        
        res = dp(0,len(s)-1)
        #print(res) 
        res[eval(s)] =5
        #print(res)
        ret = 0
        for a in answers:
            if a in res:
                ret += res[a] 
        return ret

re = Solution().scoreOfStudents("7+3*1*2", [20,13,42])
print(re)