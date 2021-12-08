from math import comb
class Solution:
    def kthSmallestPath(self, destination: list[int], k: int) -> str:
        v, h = destination
        res=""
        for i in range(v+h):
            if h ==0:
                res += "V" *v
                return res
            if v ==0:
                res += "H"*h
                return res
            vth = comb(v+h-1,h-1)
            if vth <=k:
                k -vth
                v -=1
                res +="V"
            else:
                h-=1
                res +="H"
            


re = Solution().kthSmallestPath(destination = [2,3], k = 3)           
print(re)     