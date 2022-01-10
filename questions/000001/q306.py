class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def verify(i,j):
            t1 = int(num[i:j])
            if t1 ==0:
                return True
            if t1 <(10)**(j-i-1):
                #print(i,j,t1)
                return False
            return True
        def dfs(i,a,b):
            #print(i,a,b)
            if i == n:
                return True
            c = a+b
            for j in range(i+1,n+1):
                t1 = int(num[i:j])
                if not verify(i,j):continue
                if t1 ==c:
                    return dfs(j,b,c)
            return False
        for i in range(1,n):
            for j in range(i+1,n):
                if not verify(0,i):continue
                if not verify(i,j):continue
                a = int(num[:i])
                b = int(num[i:j])
                if dfs(j, a,b):
                    return True
        return False

re = Solution().isAdditiveNumber("1023")
print(re)
                

