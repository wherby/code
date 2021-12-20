# TDK bruteforce 状态压缩 / dijstra
# https://leetcode-cn.com/contest/biweekly-contest-53/problems/minimum-xor-sum-of-two-arrays/
# https://github.com/wisdompeak/LeetCode/tree/master/BFS/1879.Minimum-XOR-Sum-of-Two-Arrays

def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        mn = 10**19
        n = len(nums1)
        dp1 = [mn] * (1<<n)
        dp2 = []
        dp1[0] =0
        for i in range(n):
            dp2 = list(dp1) # deep copy
            for state in range(1,(1<<n)):
                dp1[state] =mn
                for j in range(n):
                    if (state>>j) & 1 :
                        dp1[state] = min(dp1[state],dp2[state - (1<<j)] + (nums1[j] ^ nums2[i]) )
        return dp1[(1<<n) -1]

def minimumXORSum(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    def allState(k):
        m=n
        state = (1<<k) -1
        while (state <(1<<m)):
            for j in range(n):
                if (state>>j) & 1 :
                    dp1[state] = min(dp1[state],dp2[state - (1<<j)] + (nums1[j] ^ nums2[i]) )
            c = state &(-state)
            r = state +c
            state= (((r ^ state) >>2)//c) |r 
    mn = 10**19
    n = len(nums1)
    dp1 = [mn] * (1<<n)
    dp2 = []
    dp1[0] =0
    for i in range(n):
        dp2 = list(dp1) # deep copy
        allState(i+1)
    return dp1[(1<<n) -1]

import heapq
def minimumXORSum(self, nums1, nums2):
    n =len(nums1)
    st =[(0,0)] # (cost, state)
    visited = [0]*(1<<n)
    while st:
        cost,state = heapq.heappop(st)
        if visited[state]:continue
        if state == (1<<n)-1:return cost
        visited[state] =1
        j= bin(state).count('1')
        for i in range(n):
            if (state >>i &1): continue
            if visited(state + (1<<i)):continue
            heapq.heappush(st,(cost+ (nums1[i] ^ nums2[j]),state + (1<<i)))


