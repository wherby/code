from turtle import right


class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        leftCand ={}
        rightCand ={}
        n = len(nums)
        acc =1
        if k ==1:
            return [i for i in range(1,n-1)]
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                acc +=1
                if acc >=k and i+1 <n :
                    leftCand[i+1]=1
            else:
                acc =1
        acc =1
        for i in range(n-2,-1,-1):
            if nums[i] <=nums[i+1]:
                acc +=1
                if acc>=k and i-1>=0  :
                    rightCand[i-1]=1
            else:
                acc =1
        ret =[]
        #print(leftCand,rightCand)
        for i in range(n):
            if i in leftCand and i in rightCand:
                ret.append(i)
        return ret
        





re =Solution().goodIndices(nums = [2,1,1,1,3,4,1], k = 2)
#re =Solution().goodIndices(nums = [2,1,3], k = 1)
#re =Solution().goodIndices(nums = [878724,201541,179099,98437,35765,327555,475851,598885,849470,943442], k = 4)
print(re)