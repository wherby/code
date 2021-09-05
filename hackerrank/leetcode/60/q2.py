class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
    	def putIndic(a,b,dic1):
    		if a not in dic1:
    			dic1[a] = [b]
    		else:
    			dic1[a].append(b)

        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        dic1 = {}
        for pair in pairs:
        	a,b =pair
        	putIndic(a,b,dic1)
        	putIndic(b,a,dic1)
        m = len(words1)
        n = len(words2)
        if m != n:
        	print m,n
        	return False
        for i in range(m):
        	wt = words1[i]
        	if wt not in dic1:
        		wt2 = words2[i]
        		if wt != wt2 :
        			return False
        	else:
        		d2 = dic1[wt]
        		wt2 = words2[i]
        		if wt2 not in d2 and wt2 != wt:

        			return False
        return True



s =Solution()
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
words1 = ["one","excellent","meal"]
words2 =  ["one","good","dinner"]
print s.areSentencesSimilar(words1,words2,pairs)
