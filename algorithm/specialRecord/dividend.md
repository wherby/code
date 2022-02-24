# 乘积为某个因数倍数

https://leetcode-cn.com/contest/weekly-contest-281/problems/count-array-pairs-divisible-by-k/
给你一个下标从 0 开始、长度为 n 的整数数组 nums 和一个整数 k ，返回满足下述条件的下标对 (i, j) 的数目：

0 <= i < j <= n - 1 且
nums[i] * nums[j] 能被 k 整除。
 

示例 1：

输入：nums = [1,2,3,4,5], k = 2
输出：7
解释：
共有 7 对下标的对应积可以被 2 整除：
(0, 1)、(0, 3)、(1, 2)、(1, 3)、(1, 4)、(2, 3) 和 (3, 4)
它们的积分别是 2、4、6、8、10、12 和 20 。
其他下标对，例如 (0, 2) 和 (2, 4) 的乘积分别是 3 和 15 ，都无法被 2 整除。    

import math

class Solution(object):
    def coutPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b = b,a %b
            return a
        ls= [0]*110000
        sm = 0
        for a in nums:
            g1 = gcd(k,a)
            re = k // g1
            sm += ls[re]
            t = int(math.sqrt(g1)) 
            for j in range(1,t+1):
                if g1 %j ==0:
                    ls[j] +=1
                    if g1//j != j:
                        ls[g1//j]+=1
        return sm