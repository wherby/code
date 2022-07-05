#https://leetcode.com/submissions/detail/731644704/
#65 / 65 test cases passed.
#Status: Accepted
#Runtime: 8629 ms
#Memory Usage: 15.4 MB
class DFSWithOrder:
    def __init__(self,n,edges,nums) -> None:
        self.color=[0]*n 
        self.timeIn=[0]*n
        self.timeOut =[0]*n
        self.timer =0
        self.adj=[[] for _ in range(n)]
        self.nums = nums
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        
    def dfs(self,v):
        self.color[v] = 1
        self.timeIn[v] = self.timer
        self.timer +=1
        val = self.nums[v]
        for u in self.adj[v]:
            if self.color[u] ==0:
                self.dfs(u)
                val =val ^self.nums[u]
        self.color[v] = 2
        self.timeOut[v] = self.timer
        self.timer +=1
        self.nums[v] = val

class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        dfs= DFSWithOrder(n,edges,nums)
        dfs.dfs(0)
        mn = 10**9
        for i in range(1,n):
            for j in range(1,n):
                if i ==j : continue
                x,y,z = 0,0,dfs.nums[0]
                if dfs.timeOut[i]-dfs.timeIn[i] > dfs.timeOut[j]- dfs.timeIn[j]: continue
                if dfs.timeIn[j] <dfs.timeIn[i] and dfs.timeOut[i] < dfs.timeOut[j]:
                    x = dfs.nums[i]
                    y = dfs.nums[j] ^dfs.nums[i]
                    z = dfs.nums[0] ^dfs.nums[j]
                else:
                    x = dfs.nums[i]
                    y = dfs.nums[j]
                    z = dfs.nums[0] ^dfs.nums[j] ^dfs.nums[i]
                mn = min(mn,max(x,y,z)-min(x,y,z))
        return mn
        
re =Solution().minimumScore([9,14,2,1],[[2,3],[3,0],[3,1]])
print(re)