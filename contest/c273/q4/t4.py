from collections import defaultdict
class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic =defaultdict(int)
        for a in nums:
            dic[a] +=1
        n = len(nums)
        nums.sort()
        a0= nums[0]
        hn= n //2
        for i in range(1,n):
            if nums[i]-a0 <=0 or (nums[i]-a0) %2==1 :
                continue
            else:
                dicC = dic.copy()
                k = nums[i] -a0
                isG =True
                for j in range(n):
                    t1 = nums[j]
                    if t1 not in dicC or dicC[t1]<=0:
                        continue
                    t2 = nums[j] +k
                    if t1 in dicC and t2 in dicC and dicC[t1]>0 and dicC[t2]>0:
                        dicC[t1] -=1
                        dicC[t2] -=1
                    else:
                        isG = False
                        break
                if isG:
                    break
        res = []
        dicC = dic.copy()
        for i in range(n):
            t1 = nums[i]
            t2 = t1 + k
            if  dicC[t1]<=0 or dicC[t2] <=0:
                continue
            dicC[t1] -=1
            dicC[t2] -=1
            res.append(t1 + k //2)
        return res

re = Solution().recoverArray(nums = [11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9])
print(re)
                
                    
        