
            
from importlib.resources import Package
from re import Pattern


class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        def getACC(ls):
            acc =0
            for a in pattern:
                if a == "D":
                    acc +=1
                else:
                    acc -=1
            return acc
        k = getACC(pattern)
        dic ={}
        ret =[]
        if k >0:
            ret.append(1+k)
            dic[k+1] =1 
        else:
            ret.append(1)
            dic[1] =1
        for a in pattern:
            print(a)
            if a =="I":
                for j in range(ret[-1],10):
                    if j not in dic:
                        ret.append(j)
                        dic[j] = 1
                        break
            else:
                for j in range(ret[-1],0,-1):
                    if j not in dic:
                        ret.append(j)
                        dic[j] =1
                        break
        return ret


re =Solution().smallestNumber("IIIDIDDD")
print(re)