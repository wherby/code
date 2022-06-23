# https://leetcode.cn/problems/range-module/
import bisect
class RangeModule:

    def __init__(self):
        self.arr = []


    def addRange(self, left: int, right: int) -> None:
        res = []
        i = bisect.bisect_left(self.arr, left)
        j = bisect.bisect_right(self.arr, right)
        if i & 1 == 0:
            res.append(left)
        if j & 1 == 0:
            res.append(right)
        self.arr[i:j] = res
        
    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.arr, left)
        j = bisect.bisect_left(self.arr, right)
        return i == j and (j&1) == 1

        
    def removeRange(self, left: int, right: int) -> None:
        res = []
        i = bisect.bisect_left(self.arr, left)
        j = bisect.bisect_right(self.arr, right)
        if i & 1 :
            res.append(left)
        if j & 1 :
            res.append(right)
        self.arr[i:j] = res
        






# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

rm = RangeModule()
rm.addRange(10,20)
print(rm.arr)
rm.removeRange(14,16)
print(rm.arr)
print(rm.queryRange(10,14))
print(rm.queryRange(13,15))