# https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/submissions/
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        lo = max(jobs)
        hi = sum(jobs)
        n = len(jobs)
        jobs= sorted(jobs,reverse=True)

        def dfs(works,th,idx):
            if idx ==n:
                return True
            flag =0 ## 是否把工作分配给空闲的工人
            for j in range(k):
                if works[j] + jobs[idx] > th:
                    continue
                if works[j] ==0:
                    if flag ==1:  #如果已经分配给空闲的工人，则可以跳过
                        continue
                    else:
                        flag = 1
                works[j] += jobs[idx]
                if dfs(works,th,idx+1):
                    return True
                works[j] -=jobs[idx]
            return False

        while lo < hi:
            works = [0]*k
            mid = (lo + hi) >>1
            #print(mid)
            if dfs(works, mid,0):
                hi = mid
            else:
                lo = mid+1
        return lo

j=[256,250,255,250,254,255,260,260,250,252,257,253]
k=9
re = Solution().minimumTimeRequired(j, k )
print(re)
