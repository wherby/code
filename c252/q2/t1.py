class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        if len(milestones) ==0:
            return 0
        if len(milestones) ==1:
            return 1
        maxV = max(milestones)
        total = sum(milestones)
        if maxV >total-maxV:
            return 2*(total-maxV)+1
        else:
            return total