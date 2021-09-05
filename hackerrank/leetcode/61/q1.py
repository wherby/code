#https://leetcode.com/contest/weekly-contest-61/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        temperatures.append(101)
        re = [0]*n
        stack=[-1]
        for i in range(n):
            t1 = temperatures[i]
            while t1 > temperatures[stack[-1]]:
                w = i-stack[-1] 
                re[stack[-1]] = w
                stack.pop()
            stack.append(i)
        return re




s= Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print s.dailyTemperatures(temperatures)