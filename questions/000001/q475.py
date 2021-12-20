from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(houses)
        def isGood(r):
            start = 0
            for h in heaters:
                left = h-r
                right = h +r
                idxl = bisect_left(houses, left)
                if idxl >start:
                    return False
                idxr = bisect_right(houses,right)
                start = idxr
            if start < n:
                return False
            else:
                return True
        left = 0
        right = max(houses) + max(heaters)
        while left <right:
            mid = (left + right)>>1
            #print(left,right,isGood(mid))
            if not isGood(mid):
                left = mid+1
            else:
                right = mid
        return left

houses=[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters=[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
re = Solution().findRadius(houses , heaters)
print(re)


