#In a given array nums of positive integers, 
#find three non-overlapping subarrays with maximum sum.

#Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

#Return the result as a list of indices representing the starting position
# of each interval (0-indexed). If there are multiple answers, 
#return the lexicographically smallest one.


#Dynamic calc the maxvalue from left or right, then iterate all possible value 
#as middle one
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best
        print left,right
        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k

        return ans


if __name__=="__main__":
	nums = [1,2,1,2,6,7,5,1]
	s =Solution()
	print s.maxSumOfThreeSubarrays(nums,2)