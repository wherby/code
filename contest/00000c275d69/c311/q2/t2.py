class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        sm= 1
        n = len(s)
        acc =1
        for i in range(1,n):
            if ord(s[i])-ord(s[i-1]) ==1:
                acc +=1
                sm =max(sm,acc)
            else:
                acc =1 
        return sm




re =Solution()
print(re)