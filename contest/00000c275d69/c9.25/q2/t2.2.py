class Solution(object):
    def longestESR(self, sales):
        pre=dict({0:-1})
        res =cursum =0
        
        for i,h in enumerate(sales):
            cursum +=1 if h >8 else -1
            if cursum >0:
                res = i+1
            if cursum -1  in pre:
                res = max(res,i-pre[cursum-1])
            pre.setdefault(cursum,i)
            print(pre)
        return res
        
        

re =Solution().longestESR([11,2,4,14,2,15,7,10,1,16,9,0,2,8,4,14,6,12,2,8,6,4,14,13,7,16,14,2,3,2,8,3,12,3,3,9,14,1,5,3,12,0,15,5,0,2,3,16,7,2,1,1,4,9,0,11,9,16,15,7,0,5,6,4,12,1,1,2,13,8,3,9,12,9,3,11,4,14,7,5,16,0,11,8,8,14,1,5,0,6,5,8,10,15,9,14,16,11,1,13])
print(re)