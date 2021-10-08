from collections import defaultdict
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        res =[]
        n = len(count)
        for i in range(n):
            res += [i]*count[i]
        count = res
        a1=min(count)
        a2= max(count)
        n = len(count)
        count = sorted(count)
        a3 = sum(count)*1.000/ n
        a4 = count[n//2] if n%2==1 else (count[n//2] + count[n//2 -1])*1.0000 /2
        dic =defaultdict(int)
        mx = 0
        mxV=-1
        for i in count:
            dic[i] +=1
            if dic[i]> mx:
                mx = dic[i]
                mxV = i
        a5= mxV
        return [a1,a2,a3,a4,a5]