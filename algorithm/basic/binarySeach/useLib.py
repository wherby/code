# https://leetcode.cn/problems/maximum-number-of-alloys/submissions/
# https://leetcode.cn/circle/discuss/SwCGEn/

from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        mx = 0 
        def getCost(mid,com):
            acc = 0
            for c1,s,c in zip(com,stock,cost):
                acc += max(0,c1*mid -s ) *c
            return acc
        for com in composition:
            k = bisect_right(range(10**9),budget,key=lambda x: getCost(x,com))
            mx =max(mx,k-1)
        return mx
    
# Line 14 is bisect_right, which means need find a number which cost is more than buget,
# if ues bisect_left(range(10**9),budget,key=lambda x: getCost(x,com)) if budget could create 2.1 item, then the k will be 3, it budget could afford 3 item, then the k is 3 also 
# which is not the answer we want, if use bisect_right, then the budget could create 2.1, then k is 3, if the budget could create 3, then k is 4 , then we could use -1 to get the real k value
#  the meaning of the create 2.1:
#  getCost(2,com) < budget < getCost(3,com) which means the buget could more than afford 2 item but less than 3.
#  