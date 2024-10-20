
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0]*len(stations)
        for i,(pos,fuel) in enumerate(stations):
            for j in range(i,-1,-1):
                if dp[j]>= pos:
                    dp[j+1] = max(dp[j+1],dp[j] + fuel)
        return next((i for i,v in enumerate(dp) if v >= target),-1)