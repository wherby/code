from queue import Queue
from collections import defaultdict
class Solution(object):
    def ifNear(self,word1,word2):
        n = len(word1)
        diff =filter(lambda x: word1[x]!= word2[x],range(n))
        return len(list(diff)) ==1

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        n = len(wordList)+1
        wordList.append(beginWord)
        mx =defaultdict(list)
        for i in range(n):
            t1 = wordList[i]
            res= []
            for k in wordList:
                if self.ifNear(k,t1):
                    res.append(k)
            mx[t1] =res
        
        self.route=[]
        #print(mx)
        visited = {}
        q = Queue()
        q.put((beginWord,[beginWord]))
        while not q.empty():
            newQueue = Queue()
            cvist=[]
            while not q.empty():
                #print(list(q.queue))
                t,ls = q.get()
                if t == endWord:
                    self.route.append(ls)
                for k in mx[t]:
                    #print(k)
                    if k not in visited:
                        cvist.append(k)
                        m=list(ls)
                        m.append(k)
                        newQueue.put((k,m))
            for v in cvist:
                visited[v] =1
            q = newQueue
        if len(self.route) ==0:
            return []
        mn = min(map(lambda x: len(x),self.route))
        self.route = filter(lambda x: len(x) == mn ,self.route)
        return list(self.route)
            



        

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(Solution().findLadders(beginWord,endWord,wordList))