class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        n = len(plants)
        cnt =0
        resAic =capacityA
        resBob = capacityB
        rd = n //2
        for i in range(rd):
            if resAic >= plants[i]:
                resAic -= plants[i]
            else:
                cnt +=1
                resAic = capacityA-plants[i]
            if resBob >= plants[n-1-i]:
                resBob -= plants[n-1-i]
            else:
                cnt +=1
                resBob = capacityB - plants[n-1-i]
        if n %2 ==1:
            if max(resAic,resBob) < plants[rd ]:
                cnt +=1
        return cnt

re =Solution().minimumRefill(plants = [5], capacityA = 10, capacityB = 8)