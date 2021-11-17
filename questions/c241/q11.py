class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm =[0]
        n = len(nums)
        def all(i,tmp):
            print("cc ",tmp)
            #sm[0] += tmp
            for i in range(i,n):
                tmp2 = list(tmp)
                tmp2.append(nums[i])
                all(i+1,tmp2)

        all(0,[])

re = Solution().subsetXORSum(nums = [5,1,6])
                