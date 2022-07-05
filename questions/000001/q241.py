import functools
class Solution:
    def diffWaysToCompute(self, ex: str):
        def alldigit(ls):
            return all(x.isdigit() for x in ls)
        res = []
        n = len(ex)
        @functools.lru_cache(None)
        def dfs(l,r):
            if alldigit(ex[l:r]):
                return [int(ex[l:r])]
            ret =[]
            for i in range(l,r):
                if ex[i]=="+":
                    left =dfs(l,i)
                    right = dfs(i+1,r)
                    ret.extend([a+b for a in left for b in right])
                elif ex[i] =="-":
                    left =dfs(l,i)
                    right = dfs(i+1,r)
                    ret.extend([a-b for a in left for b in right])
                elif ex[i] =="*":
                    left =dfs(l,i)
                    right = dfs(i+1,r)
                    ret.extend([a*b for a in left for b in right])
            return ret

        res = dfs(0,n)
        return  res
                
    
    
re =Solution().diffWaysToCompute(ex = "2-1-1")
print(re)