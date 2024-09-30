# https://leetcode.cn/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        x = 1000000007
        if n ==1:
            return 3
        a = d = e = 1
        b = c = f = 0
        for i in range(n-1):
            a,b,c,d,e,f = (a+b+c+d+e+f)%x,a,b,(d+e+f)%x,d,e
        return (a+b+c+d+e+f)%x