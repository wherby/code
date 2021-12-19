class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        ls = [i for i in range(n)]
        idx = 0
        re = []
        cnt =0
        while cnt < n:
            re.append(ls[idx])
            cnt +=1
            if idx +1 <len(ls):
                ls.append(ls[idx+1])
                idx +=2
        ret =[0]*n
        for i,idx in enumerate(re):
            ret[idx] = deck[i]
        #print(ret,re)
        return ret
re =Solution().deckRevealedIncreasing([17,13,11,2,3,5,7])
