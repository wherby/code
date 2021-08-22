import copy


class Solution(object):

    def cominatrics(self, candidates, start, target, list, listin):
        if(target == 0):
            list.append(copy.copy(listin))
            return
        if(target < 0):
            return
        for i in range(start, len(candidates)):
            listin.append(candidates[i])
            self.cominatrics(candidates, i, target-candidates[i], list, listin)
            listin.pop(-1)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list = []
        self.cominatrics(candidates, 0, target, list, [])
        return list


a = Solution()
b = a.combinationSum([2, 3, 6, 7], 7)
print(b)
