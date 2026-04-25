# https://leetcode.cn/contest/biweekly-contest-180/problems/maximum-value-of-concatenated-binary-segments/description/

# 需要把全1 的先取出，
# 然后非全1 的按照 1 的个数降序，0的个数升序 做排序

class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        ttt = 10**9 + 7
        
        to_use = []
        to_rank = []
        for v1, v0 in zip(nums1, nums0) :
            if v0 == 0 :
                to_use.append([v1, v0])
                continue

            to_rank.append([v1, -v0])

        to_rank = sorted(to_rank, reverse=True)
        to_use += [[t[0], -t[1]] for t in to_rank]
        sum_all = sum(nums1) + sum(nums0)

        to_ret = 0
        for v1, v0 in to_use :
            vtemp = pow(2, v1, ttt) - 1
            vtemp *= pow(2, sum_all-v1, ttt)
            to_ret = (to_ret + vtemp) % ttt
            sum_all -= v0 + v1
        return to_ret
            