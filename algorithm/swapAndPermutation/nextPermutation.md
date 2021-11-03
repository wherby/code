#https://www.youtube.com/watch?v=xlxEm1EiD30


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
       
        maxi=nums[-1] #initilize maxi

        
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]<maxi):#checking if there is any element towards right tht is greater than present element 
                nums[i+1:]=sorted(nums[i+1:])# sort the right side from i+1 position
                j=i+1 
                while(nums[i]>=nums[j]  ):#find the next greater integer to nums[i]
                    j+=1
                nums[i],nums[j]=nums[j],nums[i]# replace the element with next greater integer  
                return
            maxi=max(maxi,nums[i])#updating the maximum element present on right side
        
        # if the list is reverse sorted 
        nums.sort()
        return 