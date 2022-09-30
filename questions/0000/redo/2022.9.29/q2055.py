from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ls=[-1]
        for i,a in enumerate(s):
            if a =="|":
                ls.append(i)
        n = len(queries)
        ret =[0]*n
        for i,(a,b) in enumerate(queries):
            idx1 = bisect_left(ls,a)
            idx2 = bisect_right(ls,b)
            if idx2 -idx1 <2:
                continue
            else:
                ret[i] = ls[idx2-1]-ls[idx1] - idx2 +idx1+1
        return ret

re = Solution().platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]])
print(re)