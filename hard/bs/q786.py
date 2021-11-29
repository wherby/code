from bisect import bisect_right,insort_left,bisect_left
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        l = 0
        r =1
        while l < r:
            mid = (l+r) /2
            cnt =0
            for i,a in enumerate(arr):
                k1 = bisect_right(arr,a *mid,0,i)
                cnt +=k1
            #print(cnt)
            
            if cnt > k:
                r =mid
            elif cnt < k:
                l = mid
            else:
                #print(mid,k,cnt)
                break
        mx = 1
        res =[1,1]
        for i,a in enumerate(arr):
            k1 = bisect_right(arr,a *mid,0,i)
            if k1 !=0:
                diff = abs(arr[k1-1] / a - mid)
                #print(diff,arr[k1-1],a)
                if abs(diff) < mx:
                    mx = diff
                    res = [arr[k1-1],a]
        return res
            

re = Solution().kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3)