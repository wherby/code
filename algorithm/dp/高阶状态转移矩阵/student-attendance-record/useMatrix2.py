# https://leetcode.cn/problems/student-attendance-record-ii/
class Solution:
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        def m_mul(a,b):
            c=[]
            for i in range(len(a)):
                c.append([])
                for j in range(len(b[0])):
                    c[-1].append(0)
                    for k in range(len(a[0])):
                        c[-1][-1]=(c[-1][-1]+a[i][k]*b[k][j])%1000000007
            return c
        ans=[[0,0,0,0,0,1]]
        a=[
            [1,1,0,0,0,0],
            [1,0,1,0,0,0],
            [1,0,0,0,0,0],
            [1,0,0,0,1,1],
            [1,0,0,0,0,1],
            [1,0,0,1,0,1]]
        while n:
            if n&1:
                ans=m_mul(ans,a)
            a,n=m_mul(a,a),n>>1
        return sum(ans[0])%1000000007