class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n = len(pref)
        ret = [0]*n
        ret[0] = pref[0]
        acc = pref[0]
        for i in range(1,n):
            ret[i] = pref[i]^ acc 
            acc = ret[i]^acc
        return ret





re =Solution().findArray( [5,2,0,3,1])
print(re)