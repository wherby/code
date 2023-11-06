from collections import deque 
# Create a deque
DoubleEnded = collections.deque
class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        mins =[100000000]
        dic ={}
        def dfs(k,i):
            print(k)
            if k >2000 or k <-2000:
                return
            if k in dic :
                return -1
            if i > 100:
                return -1
            if k ==goal:
                mins[0] = min(mins[0],i)
                return i
            dic[k] =i
            for n in nums:
                dfs(k+n,i+1)
                dfs(k-n,i+1)
                dfs(k^n,i+1)
        dfs(start,0)
        if mins[0] == 100000000:
            return -1
        
        return mins[0]
            
Solution().minimumOperations([70,83,-93,47,-81,94,64,84,4,28,37,99,42,74],95,-25)