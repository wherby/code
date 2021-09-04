from collections import defaultdict
class Solution:
    def kthLargestNumber(self, nums , k) :
        bucket =[0] *110
        bucketArr=defaultdict(list)
        for num in nums:
            n = len(num)
            bucket[n] +=1
            bucketArr[n].append(num)
        for i in range(101,-1,-1):
            k2 = k - bucket[i]
            if k2 <=0:
                arr  = bucketArr[i]
                res = []
                for t in arr:
                    res.append(int(t))
                res = sorted(res)
                #print("xx")
                #print(res)
                return str(res[len(res)-k])
            k=k2

nums = ["2","21","12","1"]
re = Solution().kthLargestNumber(nums,3)
print(re)