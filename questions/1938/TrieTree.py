#https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
#https://leetcode.com/problems/maximum-genetic-difference-query/discuss/1344900/Python-DFS-while-maintaining-a-Trie
class Trie:
    def __init__(self,*words):
        self.root =dict()
        for word in words:
            self.add(word)
    
    def add(self,word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter,dict())
        current_dict["_end_"] = True

    def __contains__(self,word):
        curent_dict= self.root
        for letter in word:
            if letter not in curent_dict:
                return False
            curent_dict = curent_dict[letter]
        return "_end_" in curent_dict
    
    ## find the nearest
    def find(self, word):
        current_dict = self.root
        res =""
        for letter in word:
            # TRY TO MATCH "1" TO "0" AND VICE VERSA
            desired = "1" if letter =="0" else "0"

            if not desired in current_dict: # if not match
                desired = letter  #set to sane
            res += desired
            current_dict = current_dict[desired]
        return res

    
    def delete(self,word):
        current_dict = self.root
        
        #nodes =[current_dict]
        objects = []
        for letter in word:
            current_dict = current_dict[letter]
            #nodes.append(current_dict)
            #print(current_dict)
            objects.append(current_dict)
        del current_dict["_end_"]

        #print(objects)
        #objects[:-1][::-1]) remove last one and reverse 
        #>>> a =[1,2,3]
        #>>> a[:-1]
        #[1, 2]
        #>>> a[:-1][::-1]
        #[2, 1]
        #>>> a
        #[1, 2, 3]
        for c, obj in zip(word[::-1],objects[:-1][::-1]):
            if not obj[c]:
                del obj[c]
            else:
                break