# Also timeout if lo =1 https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/submissions/
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        lo = max(jobs)
        hi = sum(jobs)
        n = len(jobs)
        costState = [0]*4096
        for i in range(4096):
            ret =0
            for j in range(n):
                if i & (1<<j) !=0:
                    ret += jobs[j]
            costState[i] = ret
        mem ={}
        def dfs(state,th,idx):
            #print(state,th,idx)
            if state == 0 :
                return True
            if idx ==k:
                return False
            if (idx,state) in mem:
                return False
            subSet =state
            while subSet>0:
                #print(subSet,"subset ,", idx,state)
                if costState[subSet] > th:
                    pass
                else:
                    if dfs(state -subSet,th,idx +1):
                        return True
                subSet = (subSet-1) & state
            mem[(idx,state)] =1
            return False


        while lo < hi:
            mem={}
            mid = (lo + hi) >>1
            #print(mid)
            if dfs((1<<n)-1,mid,0):
                hi = mid
            else:
                lo = mid+1
        return lo

j=[256,250,255,250,254,255,260,260,250,252,257,253]
k=9
re = Solution().minimumTimeRequired(j, k )
print(re)
               