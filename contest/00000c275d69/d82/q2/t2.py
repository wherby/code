class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses.sort()
        passengers.sort()
        st = set(passengers)
        m,n = len(buses),len(passengers)
        pidx =0
        bidx = 0
        while bidx <m:
            bs = buses[bidx]
            cnt = 0
            while cnt < capacity and pidx < n  and passengers[pidx]<=bs :
                cnt +=1
                pidx +=1
            bidx +=1
        startS = passengers[pidx-1]
        if cnt < capacity:
            startS = buses[m-1]
        while startS in st:
            startS -=1
        return startS
            
            




re =Solution().latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2)
print(re)