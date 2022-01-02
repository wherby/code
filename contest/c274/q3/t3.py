import heapq
class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        st =[]
        for a in asteroids:
            heapq.heappush(st,a)
        now = mass
        while st:
            k  = heapq.heappop(st)
            if k > now:
                return False
            now += k
        return True