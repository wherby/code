
#汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
#沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
#假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
#当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
#为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
#注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
#来源：力扣（LeetCode）
#链接：https://leetcode.cn/problems/minimum-number-of-refueling-stops
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0]*len(stations)
        for i,(pos,fuel) in enumerate(stations):
            for j in range(i,-1,-1):
                if dp[j]>= pos:
                    dp[j+1] = max(dp[j+1],dp[j] + fuel)
        return next((i for i,v in enumerate(dp) if v >= target),-1)