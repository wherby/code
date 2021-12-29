from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def numFriendRequests(self, ages) -> int:
        n= len(ages)
        cnt =0
        ages.sort()
        for i in range(n):
            x = ages[i]
            idxXMax =bisect_right(ages,x)
            idxXMax = idxXMax-1
            mn = 0.5*x +7
            idxXmin = bisect_right(ages,mn)
            cnt += max(idxXMax - idxXmin,0)
        return cnt

re = Solution().numFriendRequests( [16,17,18])
re = Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])
print(re)

# y<= 0.5x +7
#