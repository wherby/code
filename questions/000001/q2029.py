class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        tp=[0]*3
        for s in stones:
            tp[s%3] +=1
        if tp[0] %2 ==0:
            return tp[1]>0 and tp[2]>0
        else:
            return abs(tp[1]-tp[2]) >2






# 2 ,1->2->1
# 1 1 2 1 2 1 2
# 2 2 1 2 1 2 1
# 2