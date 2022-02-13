class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans = sorted(beans)
        n = len(beans)
        maxB= sum(beans)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1]  = pre[i] + beans[i]
        ret = maxB
        for i in range(n):
            numt = maxB -pre[i] - beans[i] * (n-i) + pre[i]
            ret = min(ret, numt)
        return ret