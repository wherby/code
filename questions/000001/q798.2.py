class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        diffs = [0]*n
        for i,num in enumerate(nums):
            low = (i+1)%n
            high = (i-num + n +1) %n
            diffs[low] +=1
            diffs[high] -=1
            if low >= high:
                diffs[0] +=1
        score, maxS ,idx = 0,0,0
        for i, diff in enumerate(diffs):
            score  += diff
            if score > maxS:
                maxS,idx = score,i
        return idx