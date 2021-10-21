from collections import defaultdict
from bisect import bisect_left
class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums)
        half = n //2
        sm = sum(nums)
        halfNum = sm //2

        leftDic= defaultdict(list)

        def findRes(nums):
            res =[(0,0)]
            for i in range(half):
                tp = []
                for r in res:
                    sm,num = r
                    tp.append((sm,num))
                    tp.append((sm + nums[i],num+1))
                res = list(set(tp))
            dic = defaultdict(list)
            for sm,num in res:
                dic[num].append(sm)
            return dic
        leftDic=findRes(nums[:half])
        rightDic =findRes(nums[half:])
        for i in range(half):
            leftDic[i] = sorted(leftDic[i])
            rightDic[i] = sorted(rightDic[i])
        #print(leftDic,rightDic)
        mx = sum(map(lambda x: abs(x),nums))
        for i in range(half):
            left = leftDic[i]
            right  = rightDic[half-i]
            for l in left:
                i = bisect_left(right,halfNum - l)
                    #print(l,r,sm)
                if i ==len(right):
                    r = right[-1]
                    t = l +r
                    t2 = abs(sm -t *2)
                    mx = min(mx,t2)
                else:
                    r = right[i]
                    t = l +r
                    t2 = abs(sm -t *2)
                    mx = min(mx,t2)
                    r = right[i-1]
                    t = l +r
                    t2 = abs(sm -t *2)
                    mx = min(mx,t2)
        #print(mx)
        return  mx

            

re = Solution().minimumDifference([3,9,7,3])
print(re)

