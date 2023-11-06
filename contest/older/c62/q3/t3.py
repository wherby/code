class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        n = len(answerKey)
        dpT = [0]*(n)
        dpF =[0]*(n)
        for i in range(n):
            a = answerKey[i]
            if a =="T":
                dpT[i] = dpT[i-1] +1
                dpF[i] = dpF[i-1]
            else:
                dpF[i] = dpF[i-1] +1
                dpT[i] = dpT[i-1]
        end = 1
        mx = k
        dpT =[0]+ dpT
        dpF = [0]+ dpF
        print(dpT,dpF)
        for i in range(1,n+1):
            t1 = dpT[i-1]
            if end < i:
                end = i-1 
            while end <=n and   k >= end -i+1 - (dpT[end] -t1):
                #print(end,i,dpT[end],t1,k, end -i , end -i+1 - (dpT[end] -t1))
                #print(end -i - (dpT[end] -t1),end -i)
                end = end +1
            mx = max(mx,end -i )
            #print(mx,i,end)
        end =1
        for i in range(1,n+1):
            t1 = dpF[i-1]
            if end < i:
                end = i-1 
            #print(end,i, (dpF[end] -t1))
            while end <=n and   k >= end -i +1 - (dpF[end] -t1):
                #print(end -i +1, (dpF[end] -t1))
                end = end +1
            #print(end,i)
            mx = max(mx,end -i )
            #print(mx,i,end)
        return mx


#re = Solution().maxConsecutiveAnswers("FFTFFTFFT",1)
re = Solution().maxConsecutiveAnswers("TTTTTFTFFT",2)
print(re)

