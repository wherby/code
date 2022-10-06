class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        acc =0
        dic ={}
        n = len(arr)
        for i,a in enumerate(arr):
            if a == 1:
                acc +=1
                dic[acc]= i 
        ret = [-1,-1]
        if acc ==0 and n>=3:
            return [0,2]
        if acc %3 ==0:
            m = acc //3
            a,b,c = 0,0,0
            for i in range(dic[m]):
                a = a*2 +arr[i]
            for i in range(dic[m+1],dic[2*m]):
                b = b*2 + arr[i]
            for i in range(dic[m*2+1],n):
                c = c*2 + arr[i]
            fda,fdb = False,False
            aidx,bidx = -1,-1
            for i in range(dic[m],dic[m+1]):
                a = a *2 +arr[i]
                if a ==c:
                    fda = True
                    aidx = i 
                    break
            for i in range(dic[m*2],dic[m*2+1]):
                b = b*2 + arr[i]
                if b ==c :
                    fdb =True
                    bidx =i 
                    break
            if fda and fdb:
                ret = [aidx,bidx+1]
            #print(aidx,bidx,fda,fdb,a,b,c,dic)
        return ret 

re = Solution().threeEqualParts(arr = [1,0,1,0,1])
print(re)