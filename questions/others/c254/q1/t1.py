class Solution:
    def numOfStrings(self, patterns, word) :
        re =list(filter(lambda x: word.find(x)>=0,patterns))
        return len(re)