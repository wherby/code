# https://leetcode.cn/contest/weekly-contest-520/problems/lexicographically-largest-power-array/description/
class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        curMask = (1<<15)-1
        perm =[]
        nums.sort()
        while curMask !=0 and len(nums) :
            a = nums.pop()
            perm.append(a)
            if a != curMask:
                curMask = a & curMask
                nums = [a & curMask for a in nums]
                nums.sort()
        
        power = [0] * 15
        for i in range(15):
            bit_pos = 14 - i 
            count = 0
            for x in perm:
                if (x >> bit_pos) & 1:
                    count += 1
                else:
                    break  
            power[i] = count
        return power
