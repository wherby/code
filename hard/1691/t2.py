class Solution:
    def maxHeight(self, cuboids) :
        if not cuboids:
            return 0
        for c in cuboids:
            c.sort()
        cuboids.sort(reverse = True)
        n = len(cuboids)
        print(cuboids)
        dp = [0] * n
        for i in range(n):
            for i, (l, w, h) in enumerate(cuboids):
                #print(i,l,w,h)
                dp[i] = h
                for j in range(i):
                    if cuboids[j][0] >= l and cuboids[j][1] >= w and cuboids[j][2] >= h:
                        dp[i] = max(dp[i], dp[j] + h)
                        print(dp)
        return max(dp)


cuboids = [[50,45,20],[95,37,53],[45,23,12]]
re = Solution().maxHeight(cuboids)