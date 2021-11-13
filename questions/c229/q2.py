class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        ls =[0]*n
        for i,b in enumerate(boxes):
            if b =="1":
                ls[i]=1
        lls = [0]*(n+1)
        rls= [0]*(n+1)
        pre =[0]*(n+1)
        post =[0]*(n+1)
        for i in range(n):
            lls[i+1] = lls[i] + ls[i]
            pre[i+1] = pre[i] + lls[i+1]
        for i in range(n-1,-1,-1):
            rls[i] = rls[i+1] + ls[i]
            post[i] =post[i+1] + rls[i]
        res =[]
        for i in range(n):
            t = pre[i] + post[i+1]
            res.append(t)
        #print(res)
        return res

re = Solution().minOperations("001011")
