# https://leetcode.cn/problems/smallest-substring-with-identical-characters-ii/solutions/3027031/er-fen-da-an-tan-xin-gou-zao-pythonjavac-3i4f/
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        s = [int(a) for a in s]
        n = len(s)
        def verify(mid):
            cnt = 0
            if mid == 1:
                cnt = sum([int(a== i%2) for i,a in enumerate(s)])
                cnt = min(cnt,n-cnt)
            else:
                state =0
                for i,a in enumerate(s):
                    state +=1
                    if i == n-1 or a != s[i+1]:
                        cnt += state // (mid+1)
                        state  =0
            return cnt <=numOps
        return bisect_left(range(n),True,1,key= verify)
