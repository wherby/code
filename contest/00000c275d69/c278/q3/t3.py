
class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        sr = s[::-1]
        n = len(sr)
        ls = [0]*n
        for i,a in enumerate(sr):
            ls[i] = ord(a) -ord('a') +1
        al1 = pow(power,k,modulo)
        h1 =0
        for i in range(k):
            h1 = (h1 * power + ls[i]) %modulo
        #print(h1)
        dic={}
        dic[h1]=0
        for start in range(1,n-k+1):
            h1 = (h1*power - ls[start-1]*al1 + ls[start + k -1] )% modulo
            dic[h1] =start
        start = dic[hashValue]
        #print(start,dic,hashValue)
        return sr[start:start+k][::-1]
                #return sr[start:start+k][::-1]

re =Solution().subStrHash(s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32)
print(re)