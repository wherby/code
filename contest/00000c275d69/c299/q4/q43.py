#65 / 65 test cases passed.
#Status: Accepted
#Runtime: 8451 ms
#Memory Usage: 15.8 MB
class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        color=[0]*n 
        timeIn=[0]*n
        timeOut =[0]*n
        timer =0
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(v):
            nonlocal timer
            color[v] = 1
            timeIn[v] = timer
            timer +=1
            val = nums[v]
            for u in adj[v]:
                if color[u] ==0:
                    dfs(u)
                    val =val ^nums[u]
            color[v] = 2
            timeOut[v] =timer
            timer +=1
            nums[v] = val
        dfs(0)
        mn = 10**9
        for i in range(1,n):
            for j in range(1,n):
                if i ==j : continue
                x,y,z = 0,0,nums[0]
                if timeOut[i]-timeIn[i] > timeOut[j]- timeIn[j]: continue
                if timeIn[j] <timeIn[i] and timeOut[i] < timeOut[j]:
                    x = nums[i]
                    y = nums[j] ^nums[i]
                    z = nums[0] ^nums[j]
                else:
                    x = nums[i]
                    y = nums[j]
                    z = nums[0] ^nums[j] ^nums[i]
                mn = min(mn,max(x,y,z)-min(x,y,z))
        return mn
        
re =Solution().minimumScore([9,14,2,1],[[2,3],[3,0],[3,1]])
print(re)