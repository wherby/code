# Modified from algorithm\basic\linklist\LRU\LRUCache.py
# Verified in https://leetcode.cn/problems/steps-to-make-array-non-decreasing/submissions/
#
class Node:
    def __init__(self,key,val):
        self.key =key
        self.val = val
        self.prev = self.next = None 
        
class LinkedList:
    def __init__(self) -> None:
        self.m = {}
        self.h = Node(-1000,0)
        self.t = Node(-1000,0)
        self.h.next = self.t
        self.t.prev = self.h
    
    def __delete__(self, node):
        prev =node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

    # put the element at beginning
    def newHead(self,node):
        h = self.h.next
        node.next =h 
        h.prev = node
        node.prev = self.h
        self.h.next = node
         
    def put(self,key,val):
        node = self.m.get(key,None)
        if node:
            print("Key existed")
            node.val = val
        else:
            node = Node(key,val)
            self.m[key] = node
            self.newHead(node)
            
    def newTail(self,node):
        t = self.t.prev
        node.prev = t 
        t.next = node 
        node.next = self.t 
        self.t.prev = node 
    
    def append(self,key,val):
        node= self.m.get(key,None)
        if node:
            print("Key existed")
            node.val =val
        else:
            node = Node(key,val)
            self.m[key] =node 
            self.newTail(node)
            
    def removeByKey(self,key):
        node = self.m.get(key,None)
        if not node:
            print("Key not existed:",key,self.m)
        else:
            self.__delete__(node)
            # https://stackoverflow.com/questions/5713218/best-method-to-delete-an-item-from-a-dict
            self.m.pop(node.key) #self.m.pop(node.key,None) will suppressing  error for key not existed

    def listPrint(self,node):
        while node is not None:
            print(node.key,node.val)
            node =node.next
            

dlink = LinkedList()
dlink.put(1,2)
dlink.put(2,3)
dlink.put(3,5)
dlink.append(4,5)
dlink.append(5,6)
dlink.listPrint(dlink.h)
dlink.removeByKey(4)
dlink.listPrint(dlink.h)