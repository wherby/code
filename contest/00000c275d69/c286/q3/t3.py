# 边界条件dfs
class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        m = (intLength+1) //2
        ifOdd = intLength%2 ==1
        def dfs(k,m,res,start=1):
            tm = 10**(m-1)
            #print(tm,k,m,res,k//tm)
            if k //tm >9-start:
                return []
            if m ==0:
                return res
            else:
                return dfs(k%tm,m-1,res +[k//tm +start],0)
        res=[]
        for q in queries:
            tp = dfs(q-1,m,[],1)
            if len(tp) ==0:
                res.append(-1)
            else:
                if ifOdd:
                    ttp = tp + tp[::-1][1:]
                else:
                    ttp =  tp + tp[::-1]
                t1 =0
                for a in ttp:
                    t1 = t1*10 +a
                res.append(t1)
        return res


re = Solution().kthPalindrome ([98043237],15)
print(re)