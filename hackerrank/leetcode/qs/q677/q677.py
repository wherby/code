class MapSum(object):
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

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map=MapSum.Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map.insert(key,val)

    def findNumberInNode(self,node,ls):
        for key,value in node.items():
            if key == "num":
                ls.append(value)
            else:
                self.findNumberInNode(value,ls)
        return ls
            

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        index,node1 = self.map.findLastNode(prefix)
        re1=[]
        if index== len(prefix):
            re1 =self.findNumberInNode(node1,[])
        return sum(re1)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
s= MapSum()
s.insert("apple", 3)
s.insert("apple", 4)
s.insert("app",2)
print s.sum("acp")