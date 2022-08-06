# https://leetcode.com/contest/weekly-contest-262/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
from collections import defaultdict

def getNear(ls1,ls2,val):
    mx = 10**10
    n =len(ls2)
    ridx = n-1
    for a in ls1:
        mx = min(mx,abs(a + ls2[ridx]-val))
        while ridx >0  and a + ls2[ridx]>val:
            ridx -=1
            mx =min(mx,abs(a + ls2[ridx]-val))
        mx =min(mx,abs(a + ls2[ridx]-val))
    return mx
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        half = n //2
        sm = sum(nums)
        halfsm = sm /2
        def getDic(nums):
            dic = defaultdict(set)
            st =[(0,0)]
            for a in nums:
                tst =[]
                for cnt,acc in st:
                    tst.append((cnt +1,acc +a))
                st = st+tst
            for cnt,acc in st:
                dic[cnt].add(acc)
            for k,v in dic.items():
                dic[k] = sorted(list(v))
            return dic
        leftls = getDic(nums[:half])
        rightls = getDic(nums[half:])
        mx = 10**8
        for k,v in leftls.items():
            lls = v 
            rls = rightls[half-k]
            mx = min(mx,getNear(lls,rls,halfsm))
            #print(mx,lls,rls,halfsm)
        return int(mx*2)
                
        
        

re = Solution().minimumDifference([42,41,59,43,69,67])
print(re)