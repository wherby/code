#https://leetcode.com/contest/weekly-contest-59/problems/self-dividing-numbers/
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def selfDeive(num):
        	items = []
        	tnum = num
        	while tnum !=0:
        		t1 = tnum %10
        		tnum = tnum /10
        		if t1 == 0:
        			return False
        		if num % t1 != 0:
        			return False
        	return True

        re =[]
        for i in range(left,right +1):
        	r = selfDeive(i)
        	if r == True:
        		re.append(i)
        return re





s= Solution()
print s.selfDividingNumbers(1,22)