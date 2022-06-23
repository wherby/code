# https://leetcode-cn.com/contest/weekly-contest-287/problems/encrypt-and-decrypt-strings/
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
        self.cnt =defaultdict(int)

        for k,v in zip(keys,values):
            self.dic[k] = v
            self.ddic[v].append(k)
        for a in dictionary:
            self.cnt[self.encrypt(a)] +=1            


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
        return self.cnt[word2]



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)