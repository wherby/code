import functools
class Solution:
    def diffWaysToCompute(self, ex: str):
        def alldigit(ls):
            return all(x.isdigit() for x in ls)
        n = len(ex)

        if alldigit(ex):
            return [int(ex)]
        ret =[]
        for i in range(n):
            if ex[i]=="+":
                left =self.diffWaysToCompute(ex[:i])
                right = self.diffWaysToCompute(ex[i+1:])
                ret.extend([a+b for a in left for b in right])
            elif ex[i] =="-":
                left =self.diffWaysToCompute(ex[:i])
                right = self.diffWaysToCompute(ex[i+1:])
                ret.extend([a-b for a in left for b in right])
            elif ex[i] =="*":
                left =self.diffWaysToCompute(ex[:i])
                right = self.diffWaysToCompute(ex[i+1:])
                ret.extend([a*b for a in left for b in right])
        return ret

                
    
    
re =Solution().diffWaysToCompute(ex = "2-1-1")
print(re)