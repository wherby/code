class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        ans = 1
        rest = maxSum -n
        l =r =index
        while l >0 or r < n-1:
            len = r-l +1
            if rest >= len:
                rest -= len
                ans+=1
                l = max(0,l-1)
                r = min(n-1,r+1)
            else:
                break
        ans += rest //n
        return ans