
求最小选择的时候，把状态和值一起作为比较的参数，可以减少复杂度

```py

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        invs = [(b,a,c,i) for i,(a,b,c) in enumerate(intervals)]
        invs.sort()
        n = len(invs)
        dp = [[(0,[]) for _ in range(5)] for _ in range(n+1)]
        #print(invs)
        for i,(b,a,c,idx) in enumerate(invs):
            k = bisect_left(invs,(a-1,10**19,),hi=i)  ## bisect_left()
            for j in range(1,5):
                s1,ids = dp[k][j-1]                                
                dp[i+1][j] = min(dp[i][j],(s1-c,sorted(ids + [idx])))  #用负数求最大值，把排序值一起比较自动处理相等情况
        #print(dp)
        return dp[-1][4][1]
        
```


"bisect_left(invs,(a-1,10**19,),hi=i)" 和 "bisect_left(invs,(a,),hi=i)" 等价，bisect_left 可以只提供比价的值，省略的值会是默认值？
