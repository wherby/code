class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left=-1
        right=0
        mn =0
        pOrN =True
        fistN =-1
        for i in range(n):
            t = nums[i]
            if t >0 and pOrN:
                #print("a",pOrN)
                mn = max(mn, i-left)
            elif t >0 and (not pOrN) and fistN != -1:
                #print(mn,"c",i)
                mn = max(mn,i-fistN)
            elif t ==0:
                left =i
                fistN = -1
                pOrN =True
            else:
                pOrN = not pOrN
                if pOrN ==True:
                    mn = max(mn, i-left)
                elif fistN != -1:
                    
                    mn = max(mn , i-fistN)
                if fistN == -1:
                    fistN = i     
        return mn

re = Solution().getMaxLen(nums = [-16,0,-5,2,2,-13,11,8])
print(re)