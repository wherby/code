
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -=1
        def getStep(cur,n):
            steps,first,last =0,cur,cur
            while first <=n:
                steps += min(last,n) -first +1
                first *=10
                last =last *10 +9
            return steps
        while k:
            steps =getStep(cur,n)
            if steps<=k:
                k-= steps
                cur +=1
            else:
                cur *=10
                k -=1
            #print(steps,cur,k)
        return cur

re = Solution().findKthNumber(2000000000,1111111110)
print(re)