from collections import defaultdict
class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.dic={}
        self.ddic =defaultdict(list)
        self.allow =defaultdict(dict)
        self.allowOrig ={}
        for k,v in zip(keys,values):
            self.dic[k] = v
            self.ddic[v].append(k)
        for a in dictionary:
            n = len(a)
            for i in range(1,n+1):
                self.allow[n][a[:i]] =1
            self.allowOrig[a] =1


    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        res =[]
        for a in word1:
            res.append(self.dic[a])
        return "".join(res)


    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        res=[""]
        n = len(word2)
        for i in range(0,n,2):
            a = word2[i:i+2]
            ls = self.ddic[a]
            tmp = []
            for a1 in res:
                for t in ls:
                    tmp.append(a1+t)
            res = []
            for a in tmp:
                if a in self.allow[n//2]:
                    res.append(a)
        cnt =0
        for a in res:
            if a in self.allowOrig:
                cnt  +=1
        return cnt



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)