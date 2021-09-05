#https://leetcode.com/contest/weekly-contest-58/problems/minimum-window-subsequence/
#Min SubString of SubString
#Path find

class Solution(object):
	
    def minWindow(self, S, T):
    	import bisect
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def searchPath(ls,sord,start):
        	for i in sord:
        		tp = ls[i]
        		fd = False
        		index = bisect.bisect_right(tp,start)
        		if index >= len(tp):
        			return -1
        		start = tp[index]

        		# #print tp[index]
        		# for x in tp:
        		# 	if x > start:
        		# 		start =x
        		# 		fd =True
        		# 		break
        		# if fd == False:
        		# 	return -1
        	return start
        ls =[]
        for i in range(26):
        	ls.append([])
        n = len(S)
        for i in range(n):
        	t = S[i]
        	ls[ord(t) -ord('a')].append(i)
        sord = []
        for i in T:
        	sord.append(ord(i) -ord('a'))
        re = ls[sord[0]]
        sord =sord[1:]
        re2 = map(lambda x:searchPath(ls,sord,x),re)
        n = len(re)
        minLen=len(S)
        res =""
        for i in range(n):
        	if re2[i] ==-1:
        		break
        	tp = S[re[i]:re2[i]+1]
        	if len(tp)< minLen:
        		res = tp
        		minLen = len(tp)
        return res


s= Solution()
s.minWindow("cnhczmccqouqadqtmjjzl","mm")