import collections
from queue import Queue
from collections import defaultdict
import queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        mydict = defaultdict(int)

        for word in wordList:
            mydict[word] =0
        
        queue = collections.deque()
        visited =set()
        queue.append((beginWord,1))
        visited.add(beginWord)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        while queue:
            curr,depth = queue.popleft()
            if curr == endWord:
                return depth
            for i in range(len(curr)):
                for c in alphabets:
                    newWord = curr[:i] + c +curr[i+1:]
                    if newWord not in visited and newWord in mydict:
                        queue.append((newWord,depth +1))
                        visited.add(newWord)
        return 0