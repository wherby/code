class Solution(object):
    def maxHeight(self, cuboids):
        n = len(cuboids)
        cubs =[]
        for cub in cuboids:
            cubs.append(sorted(cub))
        cubs = sorted(cubs)
        dp = [0]*n
        for i in range(n):
            dp[i] = cubs[i][2]
            a =cubs[i]
            for j in range(i):
                 b = cubs[j]
                 if a[0]>=b[0] and a[1] >=b[1] and a[2]>=b[2]:
                     dp[i] = max(dp[i], dp[j] + a[2],dp[j])
        return max(dp)



cuboids = [[38,25,45],[76,35,3]]
re = Solution().maxHeight(cuboids)
print(re)