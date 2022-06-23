class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        dic={}
        mn = 100000000
        for i,a in enumerate(cards):
            if a not in dic:
                dic[a] =i
            else:
                t = i+1 - dic[a]
                mn = min(mn,t)
                dic[a] =i
        return mn if mn < 1000000 else -1