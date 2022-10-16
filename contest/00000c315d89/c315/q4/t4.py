from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        lls = []
        tmp =[]
        nums.append(maxK+1)
        for a in nums:
            if minK <=a <=maxK:
                tmp.append(a)
            else:
                if len(tmp) >0:
                    lls.append(tmp)
                tmp=[]
        cnt =0
        
        for ls in lls:
            last =-1
            n = len(ls)
            sl = SortedList()
            for i,a in enumerate(ls):
                if a == minK:
                    sl.add((i,1))
                if a == maxK:
                    sl.add((i,-1))
            m = len(sl)
            #print(sl)
            for i in range(1,m):
                a1,f1= sl[i]
                a2,f2= sl[i-1]
                if f1*f2<1:
                    cnt +=(a2-last)*(n-a1)
                    #print(cnt, a1-last,n-a2,n,a1,a2)
                    last = a2
                
        return cnt
                    

## 32123123
## * 0 *0 *
  


re =Solution().countSubarrays([978650,978650,978650,68071,52201,68071,186141,978650,978650,267135,68071,717241,242895,68071,582505,978650,68071,68071],68071,978650)
print(re)