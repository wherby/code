

# 

https://leetcode.cn/contest/weekly-contest-426/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description/


这个问题可以用奇偶性解决
https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/solutions/3006331/an-qi-ou-fen-lei-pythonjavacgo-by-endles-dweg/

但是比赛中用了树上dp的特性，但是这个问题有个坑是如果用cache方式解决，在每次运行子问题的时候需要 dfs.cache_clear()， 因为两个子问题有重叠的值域
如果是菊花形状的图，则会超时。

```python
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        

        def getls(edgs,isGood):
            n = len(edgs ) +1
            g= [[] for _ in range(n)]
            for a,b in edgs:
                g[a].append(b)
                g[b].append(a)
            ret = [0]*n
            @cache
            def dfs(a,p,isGood):
                ret = int(isGood)
                for b in g[a]:
                    if b ==p:continue
                    ret += dfs(b,a,not isGood)
                return ret

            for i in range(n):
                ret[i]=dfs(i,-1,isGood)
                #print(i,dfs(i,-1,k))
            dfs.cache_clear()
            return ret
        ls1 = getls(edges1,True)
        ls2 =getls(edges2,False)
        b = max(ls2)
        return [a+b for a in ls1]
```