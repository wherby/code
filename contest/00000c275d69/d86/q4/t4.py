from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        n = len(chargeTimes)
        ret = 0
        pls = [0]*(n+1) 
        for i,a in enumerate(runningCosts):
            pls[i+1] = pls[i]+a
        left,right=0,0
        sl = SortedList([])
        for i in range(n):
            sl.add(chargeTimes[i])
            mx = sl[-1]
            while left<=i and mx + (pls[i+1]-pls[left])*(i-left +1)>budget:
                sl.remove(chargeTimes[left])
                left +=1
            ret = max(ret,i+1-left)
        return ret



re =Solution().maximumRobots(chargeTimes = [19,63,21,8,5,46,56,45,54,30,92,63,31,71,87,94,67,8,19,89,79,25],
                             runningCosts = [19,63,21,8,5,46,56,45,54,30,92,63,31,71,87,94,67,8,19,89,79,25], budget = 85)
print(re)