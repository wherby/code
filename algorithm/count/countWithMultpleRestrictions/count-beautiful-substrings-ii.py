# https://leetcode.cn/contest/weekly-contest-373/problems/count-beautiful-substrings-ii/

class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        t=1 
        while t*t%(4*k):
            t +=1
        dic={}
        dic[(0,t-1)]=1 # 多个限制就变成多维的key
        sm = 0
        vl=set(['a','e','i','o','u'])
        acc =0
        for i,a in enumerate(s):
            if a in vl:
                acc +=1
            else:
                acc -=1
            sm += dic.get((acc,i%t),0)
            dic[(acc,i%t)] = dic.get((acc,i%t),0) +1
        return sm