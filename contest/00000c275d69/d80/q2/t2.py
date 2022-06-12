from bisect import bisect_right,insort_left,bisect_left
import math
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(spells)
        ret =[0]*n
        potions.sort()
        m = len(potions)
        for i,s in enumerate(spells):
            k = math.ceil(success /s) 
            kidx = bisect_left(potions,k)
            # if kidx<n and   potions[kidx] ==k:
            #     kidx -=1
            ret[i] =max( m - kidx,0)
        return ret

re =Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7)
print(re)