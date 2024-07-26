# https://leetcode.cn/contest/weekly-contest-402/problems/peaks-in-array/

# contest\00000c397d130\c402\q4\t4 copy.py

from typing import List, Tuple, Optional

class NumArray:
    def __init__(self, nums: List[int]):
        self.raw = [t for t in nums]
        T = 2
        while T <= len(nums) :
            for i in range(T, len(nums)+1, T) :
                nums[i-1] += nums[i-1-T//2]
            T = T * 2
        self.nums = nums
        self.lowbit = lambda x : x&(-x)

    def update(self, index: int, val: int) -> None:
        if val == self.raw[index] :
            return
        dis = val - self.raw[index]
        self.raw[index] = val
        while index < len(self.nums) :
            self.nums[index] += dis
            index += self.lowbit(index+1)

    def presums(self, index) :
        to_ret = 0
        while index >= 0 :
            to_ret += self.nums[index]
            index -= self.lowbit(index+1)
        return to_ret

    def sumRange(self, left: int, right: int) -> int:
        return self.presums(right)-self.presums(left-1)
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        na_raw = [0] * len(nums)
        for i in range(1, len(nums)-1) :
            if nums[i] > nums[i-1] and nums[i] > nums[i+1] :
                na_raw[i] = 1
        na = NumArray(na_raw)
        
        def check_p(v1) :
            new_v = 0
            if 0 < v1 < len(nums)-1 :
                if nums[v1] > nums[v1-1] and nums[v1] > nums[v1+1] :
                    new_v = 1 
            return new_v
        
        to_ret = []
        for tp, v1, v2 in queries :
            # print(na.raw)
            if tp == 1 :
                if not v2-1 >= v1+1 :
                    to_ret.append(0)
                else :
                    to_ret.append(na.sumRange(v1+1, v2-1))
            else :
                nums[v1] = v2
                na.update(v1, check_p(v1))
                if v1-1 >= 0 :
                    na.update(v1-1, check_p(v1-1))
                if v1+1 < len(nums) :
                    na.update(v1+1, check_p(v1+1))
        return to_ret