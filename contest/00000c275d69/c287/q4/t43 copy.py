from collections import defaultdict
import random
class Encrypter(object):
    def rollingHashDoubleHash(self,start,char):
        return (start *self.a1 + ord(char)) %self.mod1
    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        # 生成两个进制
        self.a1 = random.randint(26, 100)
        # 生成两个模
        self.mod1 = random.randint(10**9+7, 2**31-1)

        self.dic={}
        self.ddic =defaultdict(list)
        self.allow =defaultdict(int) 
        self.allowOrig ={}
        for k,v in zip(keys,values):
            self.dic[k] = v
            self.ddic[v].append(k)
        for a in dictionary:
            n = len(a)
            start = 1
            for i in range(n):
                start = self.rollingHashDoubleHash(start,a[i])
                self.allow[start] =i
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
        res=[1]
        n = len(word2)
        for i in range(0,n,2):
            a = word2[i:i+2]
            ls = self.ddic[a]
            tmp = []
            for a1 in res:
                for t in ls:
                    tmp.append(self.rollingHashDoubleHash(a1,t))
            res = []
            for a in tmp:
                if a in self.allow and self.allow[a] == i//2:
                    res.append(a)
            res = list(set(res))
            #print(res)
        return len(res)



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)