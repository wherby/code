class Solution(object):
    def minOperations(self, boxes):
        n= len(boxes)
        dp =[0]*n
        right =0
        for i in range(n):
            if boxes[i] == "1":
                dp[0] +=i
                right +=1
        left = 0
        for j in range(1,n):
            if boxes[j-1] =="1":
                left +=1
                right -=1
            dp[j] = dp[j-1] -right +left
        return dp

re = Solution().minOperations("001011")
print(re)