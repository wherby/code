from collections import defaultdict
class Trie:
    def __init__(self):
        self.root =dict()
        self.NoFound =set()
    
    def add(self,word,indx):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                self.NoFound.add(indx)
            current_dict = current_dict.setdefault(letter,dict())
        current_dict["_end_"] = True

class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        favoriteCompanies =list(enumerate(favoriteCompanies))
        fas = sorted(favoriteCompanies,key=lambda x: -len(x[1]))
        tri = Trie()
        for f in fas:
            indx,word = f
            word =sorted(word)
            tri.add(word,indx)
        #print(tri.NoFound)
        return sorted(list(tri.NoFound))

favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]

re =Solution().peopleIndexes(favoriteCompanies)
print(re)          
