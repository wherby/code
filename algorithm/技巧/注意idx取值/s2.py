


import heapq
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 10**100
        def getNumb(nums):
            nonlocal ret
            n3 = len(nums)
            n = n3 //3
            st1 =[]
            st2 =[]
            for i in range(n):
                heapq.heappush(st1,-nums[i])
            left = sum(nums[:n])
            leftls=[left]
            for i in range(n,n*2):
                #print(st1[0],nums[i])
                if -st1[0] > nums[i]:
                    left = left +st1[0] + nums[i]
                    heapq.heappop(st1)
                    heapq.heappush(st1,-nums[i])
                leftls.append(left)
            right = sum(nums[n*2:n3])
            for i in range(n*2,n3):
                heapq.heappush(st2,nums[i])
            rightls=[right]
            for i in range(n*2-1,n-1,-1):
                if st2[0] <nums[i]:
                    right = right - st2[0] +nums[i]
                    heapq.heappop(st2)
                    heapq.heappush(st2,nums[i])
                rightls.append(right)
            rightls =rightls[::-1]
            m = len(leftls)
            
            #print(leftls,rightls)
            for i in range(m):
                ret = min(ret, leftls[i] -rightls[i])
        getNumb(nums)
        return ret