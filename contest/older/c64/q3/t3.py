from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ps = []
        cs =[]
        n =len(s)
        psidx =[0] *n
        cnt =0
        for i,a in enumerate(s):
            if a == "*":
                ps.append(i)
                cnt  +=1
            else:
                cs.append(i)
            psidx[i]  = cnt
        #print(psidx,ps,cs)
        res =[]
        for q in queries:
            l,r = q
            #print(l,r)
            lc = bisect_left(cs,l)
            rc = bisect_left(cs,r)
            left = cs[lc]
            right = 0
            if rc >= len(cs):
                right = cs[-1]
            elif r !=cs[rc]:
                right =cs[rc -1]
            else:
                right =cs[rc]
            t =max(0, psidx[right] -psidx[left])
            res.append(t)
        return res



s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
re = Solution().platesBetweenCandles(s,queries)
print(re)