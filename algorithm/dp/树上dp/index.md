
# 树上dp

可以先处理dp 子数组，然后再加上节点返回

```python
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        g = [[] for _ in nums]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(a,p):
            f0,f1 = 0,-10**20
            for b in g[a]:
                if b != p :
                    r0,r1 = dfs(b,a)
                    f0,f1 = max(f0+r0, f1 + r1 ), max(f1+r0,f0+r1)
            return max( f0 + nums[a], f1 + (nums[a]^k)), max(f1 + nums[a], f0 + (nums[a]^k))
        return dfs(0,-1)[0]  
```