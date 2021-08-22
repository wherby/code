
from bisect import bisect_left
class Solution(object):
    # def getNumbers(self,zod,ood,tod,zindx,oidx,tidx):
    #     k = zod[zindx]
    #     while ood[oidx] <k and oidx < len(ood):
    #         oidx +=1
    #     while tod[tidx] <k and tidx <len(tod):
    #         tidx +=1
    #     if ood[oidx] <k or tod[tidx]<k:
    #         return 0
    #     return ((len(ood) -oidx) * (len(tod)-tidx),oidx,tidx)
    def comB(self,n):
        if n ==0:
            return 0
        if n ==1:
            return 1
        #print(n,2**n-1)
        return 2**n-1

    def getNumbers(self,zod,ood,tod,ostart,oend):
        zindex = bisect_left(zod,ostart)
        tindex = bisect_left(tod,oend)
        # print(zindex,tindex,ostart,oend,"vb")
        # print(self.comB(zindex),zindex,"zindx")
        # print(self.comB( (len(tod) -tindex)),(len(tod) -tindex),"aaa")
        return self.comB(zindex) * self.comB( (len(tod) -tindex))

    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        CONSTA = 10**9 +7
        zod =[]
        ood =[]
        tod =[]
        for i in range(len(nums)):
            k = nums[i]
            if k ==0:
                zod.append(i)
            if k == 1:
                ood.append(i)
            if k == 2:
                tod.append(i)
        sm =0
        zidx =0
        oidx =0
        tidx =0
        for i in range(len(ood)):
            ostart = ood[i]
            for j in range(i, len(ood)):
                oend = ood[j]
                mt=1
                if i+1 <j:
                    #print(j,i,"cccc")
                    mt = 2**(j-i)
                res = self.getNumbers(zod,ood,tod,ostart,oend)*mt
                #print(res,ostart,oend,mt,self.getNumbers(zod,ood,tod,ostart,oend),mt ,"ddebug")
                sm =(res+sm)%CONSTA
        return sm

print(Solution().countSpecialSubsequences( [2,0,0,2,0,1,2]))
