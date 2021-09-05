##Time Limit Exceeded
class WordFilter(object):

    class Trie(object):
        def __init__(self):
            self.root = dict()

        def insert(self, string,num):
            index, node = self.findLastNode(string)
            for char in string[index:]:
                new_node = dict()
                node[char] = new_node
                node = new_node
            node["num"] =num

        def find(self, string):
            index, node = self.findLastNode(string)
            return (index == len(string))

        def findLastNode(self, string):
            '''
            @param string: string to be searched
            @return: (index, node).
                index: int. first char(string[index]) of string not found in Trie tree. Otherwise, the length of string
                node: dict. node doesn't have string[index].
            '''
            node = self.root
            index = 0
            while index < len(string):
                char = string[index]
                if char in node:
                    node = node[char]
                else:
                    break
                index += 1
            return (index, node)


    def __init__(self, words):
        
        """
        :type words: List[str]
        """
        self.ls=WordFilter.Trie()
        self.rls=WordFilter.Trie()
        cnt =0
        self.dic={}
        for index ,word in enumerate(words):
            #print index,word
            rword = word[::-1]
            self.ls.insert(word,index)
            self.rls.insert(rword,index)

        #print self.ls,self.rls
    
    def findNumberInNode(self,node,ls):
        for key,value in node.items():
            if key == "num":
                ls.append(value)
            else:
                self.findNumberInNode(value,ls)
        return ls
            

    def f(self, prefix, suffix):
        re1 = []
        re2 = []
        suffix = suffix[::-1]
        if self.ls.find(prefix):
            index,node1 = self.ls.findLastNode(prefix)
            re1 =self.findNumberInNode(node1,[])
        if self.rls.find(suffix):
            index2,node2 = self.rls.findLastNode(suffix)
            re2 = self.findNumberInNode(node2,[])
        num = -1
        dic1 = {}
        for i in re1:
            dic1[i] =1
        for j in re2:
            if j in dic1:
                if j > num:
                    num = j
        return num
        


w = WordFilter(["pop","cas","zca","dre"])
print w.f("aa", "e")
print w.f("p", "op")
        