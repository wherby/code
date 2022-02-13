from collections import defaultdict
class Solution(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        n  = len(nums)
        m = numSlots
        dic= defaultdict(int)
        for i in range(1,m+1):
            dic[i] =2
        ret  =0
        noMatch = []
        noMatchDic =defaultdict(int)
        for a in nums:
            if dic[a] >0:
                ret += a
                dic[a] -=1
                #print(a)
            else:
                noMatch.append(a)
                noMatchDic[a]+=1
        print(ret,noMatch,dic)
        dicR = {}
        for i in range(16):
            ls=[]
            for k,v in noMatchDic.items():
                if v >0:
                    ls = ls + [k]*v
            noMatch = ls
            for x,a in enumerate(noMatch):
                #print("aa",i,a,noMatch)
                for j in range(1,m+1):
                   # print(a,i,j,a&j)
                    if a -(a &j) == i and dic[j] >0:
                        #print(ret,dic)
                        #print(ret,noMatch)
                        ret  += (a &j)
                        dic[j] -=1
                        noMatchDic[a]-=1
                        print(ret,a,j,a&j)
                        break
        return ret


        

re = Solution().maximumANDSum(nums = [10,10,1,3,6,13,2], numSlots = 8)
print(re)
re = Solution().maximumANDSum(nums = [4,2,2,11,7,12,9,8], numSlots = 4)
print(re)