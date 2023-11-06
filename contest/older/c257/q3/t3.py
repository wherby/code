class Solution:
    def firstDayBeenInAllRooms(self, nextVisit) :
        n = len(nextVisit)
        dp=[[-1,-1] for i in range(n)]
        cnt =0
        q= []
        visted={}
        while len(visted):


nextVisit = [0,0,2]
re = Solution().firstDayBeenInAllRooms(nextVisit)
print(nextVisit)