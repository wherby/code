#https://discuss.leetcode.com/topic/113487/python-simple-solution
#Since the prefix and suffix lengths are small, we can simply use a hash table.
#For each word, for all possible combinations of its prefixes and suffixes, we save the result in the hash table.

#Time: O(N)
#For each word, we update hash table entries corresponding to up to 121 prefix-suffix combinations.
#Space: O(N)
#For each word, we can create at most 121 prefix-suffix keys in the hash table.

class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ht = {}

        for W, w in enumerate(words):
            pre = ""
            L = len(w)
            for i in range(-1, min(10, L)): # first i letters form the prefix
                suf = ""
                if i != -1:
                    pre += w[i]
                for j in range(-1, min(10, L)): # last j letters form the suffix
                    if j != -1:                              
                        suf += w[-(j+1)]
                    self.ht[pre + "$" + suf] = W

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        key = prefix + "$" + suffix[::-1]
        if key not in self.ht:
            return -1
        return self.ht[key]

w = WordFilter(["pop","cas","zca","dre"])
print w.f("aa", "e")
print w.f("p", "op")