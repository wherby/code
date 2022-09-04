class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            tmp =[]
            k = n 
            while k:
                t = k %i 
                k = k//i 
                tmp.append(t)
            if tmp != reversed(tmp):
                return False
        return True    





re =Solution()
print(re)