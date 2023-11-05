from bisect import bisect_right
class Solution(object):
    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        packages.sort()
        n = len(packages)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i] + packages[i]
        pre
        #print(pre)
        maxP = packages[-1]
        m = len(boxes)
        boxesRe = []
        for i in range(m):
            boxes[i].sort()
            if boxes[i][-1] >= maxP:
                boxesRe.append(boxes[i])
        mn = -1
        res = []
        for box in boxesRe:
            cnt = 0
            idx = 0
            for b in box:
                idp = bisect_right(packages,b)
                t = b*(idp -idx) - (pre[idp]-pre[idx])
                cnt += t
                idx = idp
                #print(t,b,idp,idx)
            res.append(cnt)
        #print(res)
        if len(res ) == 0:
            return -1
        else:
            mn = min(res)
            return mn %(10**9+7)

            

re = Solution().minWastedSpace(packages = [2,5,3], boxes = [[8,4],[2,8]])
print(re)