# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# 实现一个对象缓存池
# 能够存储的个数有上限: 10K
# 实现一个淘汰的算法
# get, set 
# 操作性能和dict相当


class Node:
    def __init__(self,value):
        self.value = value 
        self.left = null
        self.right = null


class pool:
    def __init__(self):
        self.dic1 = {}
        self.length = 0
        self.MaxLen = 1000
        self.head =null
        self.last=null

    
    def setKey(self,key,value):
        if key not in self.dic1:
            if self.length < self.MaxLen:
                node = Node(value)
                if self.head == null:
                    self.head = node
                node.left = self.last
                self.last.right = node
                self.last = node
                self.dic1[key] = value
                self.length = self.length +1
            else:
                self.removeLastKey()
                node = Node(value)
                node.left = self.last
                self.last.right = node
                self.last = node
                self.dic1[key] = node
        else:
            tempNode = self.dic1[key]
            tempNode.left.left.right = tempNode.right
            tempNode.left  =self.last
            self.last.right = tempNode
            self.last = tempNode
            self.dic1[key] = node
            
            
   
    def getKey(self, key,value):
        if key not in self.dic1:
            return null
        else:
            tempNode = self.dic1[key]
            tempNode.left.left.right = tempNode.right
            tempNode.left = self.last
            self.last.right = tempNode
            self.last = tempNode
            return self.dic1[key]
   
    def removeLastKey():
        tempNode = self.head
        self.head.right.right.left = self.head
        self.head= self.head.right 
       
        del self.dic1[tempNode.key]
        