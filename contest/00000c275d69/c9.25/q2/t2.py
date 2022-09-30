from turtle import st


class Solution(object):
    def longestESR(self, sales):
        """
        :type sales: List[int]
        :rtype: int
        """
        n = len(sales)
        ls =[0]
        for a in sales:
            if a >8:
                ls.append(ls[-1] +1)
            else:
                ls.append(ls[-1])
        def verify(k):
            #print(k,n,n-k+1)
            for i in range(n-k+1):
                #print(i,k)
                if (ls[i+k] -ls[i])*2 > k  :
                    return True
            return False
        if ls[-1]*2 >n:
            return n
        start =1
        startIndx =0
        isGood =True
        while isGood:
            fd = False
            for i in range(startIndx,n-start):
                if (ls[i +start] -ls[i])*2 > start:
                    fd = True
                    break
                else:
                    pass
                    #startIndx =i+2
            if fd == False:
                print(startIndx)
                return max(0,start-2)
            else:
                start +=2
        return start-2




re =Solution().longestESR([14,7,6,14,15,0,3,4,10,5,1,8,16,7])
re =Solution().longestESR([11,2,4,14,2,15,7,10,1,16,9,0,2,8,4,14,6,12,2,8,6,4,14,13,7,16,14,2,3,2,8,3,12,3,3,9,14,1,5,3,12,0,15,5,0,2,3,16,7,2,1,1,4,9,0,11,9,16,15,7,0,5,6,4,12,1,1,2,13,8,3,9,12,9,3,11,4,14,7,5,16,0,11,8,8,14,1,5,0,6,5,8,10,15,9,14,16,11,1,13])
print(re)