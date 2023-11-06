from sortedcontainers import SortedList
import heapq
class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]+ nums[i]
        mx =0
        #print(pre,sum(nums))
        q=[]
        sl = SortedList([(0,n-1)])
        for i,n in enumerate(nums):
            heapq.heappush(q,(n,i))
        while q:
            t,iq = heapq.heappop(q)
            res = [iq]
            while q and q[0][0] ==t:
                t,iq = heapq.heappop(q)
                res.append(iq)
            res.sort()
            for iq in res:
                tp =(iq,iq+1)
                idx = sl.bisect_right(tp)
                if idx ==0:
                    left,right =sl[idx]
                else:
                    left,right =sl[idx-1]
            
                mx = max(mx,t * (pre[right+1] - pre[left]))
                if idx== 0:
                    sl.pop(idx)
                else:
                    #print(iq,sl)
                    sl.pop(idx-1)
                #print(sl)
                if iq-1>=left:
                    sl.add((left,min(iq-1,right)))
                if iq +1 <= right:
                    sl.add((iq+1,right))
                #print(t,iq,idx,left,right,mx,sl,left,right)
        return mx
            

re = Solution().maxSumMinProduct([3,3,2,2,3,1,1,4,1,3])
print(re)