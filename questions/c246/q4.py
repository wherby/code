class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        tmp = [0]*101
        pre=[list(tmp)]
        for n in  nums:
            tmp[n] +=1
            pre.append(list(tmp))
        ret =[]
        for a,b in queries:
            ta = pre[a]
            tb = pre[b+1]
            res =[]
            for i in range(1,101):
                if tb[i] -ta[i]>0:
                    res.append(i)
            #print(res,len(res))
            if len(res) <2:
                print("cc")
                ret.append(-1)
            else:
                mx = 100
                for i in range(1,len(res)):
                    mx = min(mx, res[i]-res[i-1])
                ret.append(mx)
        return ret

re = Solution().minDifference(nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]])
print(re)
            
