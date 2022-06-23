
class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)

class NumArray:

    def __init__(self, nums):
        self.ft= FenwickTree(nums)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] =val
        self.ft.add(index,delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.ft.sumTo(right) - self.ft.sumTo(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

a = NumArray([1, 3, 5])
print(a.ft.bit)
re =a.sumRange(0,2)
print(re)
a.update(1,2)
re = a.sumRange(0,2)
print(re)
print(a.ft.bit)