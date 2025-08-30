# https://leetcode.com/contest/weekly-contest-464/problems/jump-game-ix/
# 寻找某个点最多能往右跳的到index的距离，
# 
    # a,b,c 
    # b >c 
    # a> b 
# 

# [9,30,16,6,36,9]
# 对于第1个9而言，只能跳到6的位置， 但是6 可以继续跳到16 的位置，16又可以跳到最后一个9的位置
# 所以需要把每个点和它能跳到的最右点用DSU连接起来
# 所以需要用dsu 查找最多能跳到最右的位置 
# algorithm/stack/DSUWithStack/t3.py 就是错误的结果，因为只有一次跳跃

from typing import List, Tuple, Optional
from collections import defaultdict,deque
from bisect import bisect_right,insort_left,bisect_left
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        self.p[self.find(x)] =self.find(y)
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rst= deque([])
        mx = nums[0]
        ret = [0]*n 
        for i in range(n):
            mx = max(nums[i],mx)
            ret[i] =mx
        dsu = DSU(n)
        for i in range(n-1,-1,-1):
            if len(rst) ==0:
                rst.append(i)
            elif nums[rst[0]]> nums[i]:
                rst.appendleft(i)
            kidx = bisect_left(rst,max(nums[i],ret[i]),key=lambda x: nums[x])
            # if kidx< len(rst):
            #     print(nums[i],rst,kidx,i,nums[rst[kidx]],rst[kidx])
            if kidx >0:
                #ridx[i] = rst[kidx-1]
                dsu.union(i,rst[kidx-1])
            print(rst,[dsu.find(j) for j in range(n)],i)
        #print(ridx)
        pre = [0]*n 
        for i,a in enumerate(nums):
            pre[i] = max(pre[i-1],a)
        
        for i,a in enumerate(nums):
            ret[i] = max(a,pre[dsu.find(i)],ret[i])
        return ret

re =Solution().maxValue([9,30,16,6,36,9])
print(re)