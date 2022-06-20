class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num ==0:
            return 0
        if  k ==0:
            if num%10 !=0:
                return -1
            else:
                return 1
        ret = num%10
        for i in range(10):
            ac  = i*10 + ret 
            if ac <=num and ac%k ==0 and ac >=k:
                return ac //k 
        return -1

re = Solution().minimumNumbers(1,1)
print(re)