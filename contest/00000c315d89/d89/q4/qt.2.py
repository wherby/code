class Solution(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        tree = [[] for _ in nums]
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def fn(u,p):
            ans = nums[u]
            for v in tree[u]:
                if v!=p: ans +=fn(v,u)
            return 0 if ans == cand else ans 
        total = sum(nums)
        for cand in range(1,total //2 +1):
            if total % cand ==0 and fn(0,-1)==0: return total//cand -1
        return 0