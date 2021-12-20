# 时间比状态压缩花费多
import heapq
class Solution(object):
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
                newState = state + (1<<i)
                if visited[newState]:continue
                heapq.heappush(st,(cost+ (nums1[i] ^ nums2[j]),state + (1<<i)))


re = Solution().minimumXORSum(nums1 = [1,2], nums2 = [2,3])
print(re)

# Dijstra  BFS + PQ
# state = 000000=> 000001
#               => 000010
#               => 000100
#               => 100000