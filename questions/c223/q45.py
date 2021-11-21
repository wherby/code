#https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1009859/Python3-backtracking
class Solution:
    def minimumTimeRequired(self, jobs, k) :
        n = len(jobs)
        time = [0]*k
        def fn(i):
            nonlocal ans
            if i == n :
                ans = max(time)
            else:
                for kk in range(k):
                    if not kk or time[kk-1] != time[kk]:
                        time[kk] += jobs[i]
                        if max(time) < ans:
                            fn(i+1)
                        time[kk] -= jobs[i]
        ans = 10**10
        fn(0)
        return ans

j=[256,250,255,250,254,255,260,260,250,252,257,253]
k=9
re = Solution().minimumTimeRequired(j, k )
print(re)
