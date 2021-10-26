#https://leetcode.com/contest/weekly-contest-237/problems/maximum-ice-cream-bars/
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        cnt = 0
        while cnt <len(costs) and  coins >= costs[cnt]:
            coins = coins - costs[cnt]
            cnt +=1
        return cnt