class Node:
    def __init__(self,value,pre =None,next=None,key =None):
        self.val = value
        self.next = next 
        self.pre = pre
        self.key = key

class LRU:
    def __init__(self,n):
        self.cnt = n 
        self.dic = {}
        self.head = Node(-1)
        self.tail = self.head
    
    def insert(self,t):
        t.pre =self.tail
        self.tail.next = t
        self.tail = t
    
    def remove(self,t):
        if t.next:
            t.next.pre = t.pre
        t.pre.next = t.next
       # print(t.key,"a",self.dic)
        del self.dic[t.key]

    def removeHead(self):
        t = self.head.next
        self.remove(t)
    
    def get2(self,key):
        if key in self.dic:
            t = self.dic[key]
            self.remove(t)
            self.insert(t)
            self.dic[key] = t
            return t.val
        else:
            return -1
    
    def get(self,key):
        t = self.get2(key)
        print(t)
        return t
    
    def put(self,key,value):
        if key in self.dic:
            t = self.dic[key]
            self.remove(t)
            t = Node(value,None,None,key)
            self.insert(t)
        elif self.cnt ==0:
            self.removeHead()
           # print("a",self.dic)
            t = Node(value,None,None,key)
            self.insert(t)
        else:
            self.cnt -=1
            t = Node(value,None,None,key)
            self.insert(t)
        self.dic[key] =  t


lRUCache = LRU(2)
lRUCache.put(1, 1); #// cache is {1=1}
lRUCache.put(2, 2);# // cache is {1=1, 2=2}
lRUCache.get(1);   # // return 1
lRUCache.put(3, 3);# // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);   # // returns -1 (not found)
lRUCache.put(4, 4);# // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);  #  // return -1 (not found)
lRUCache.get(3); #   // return 3
lRUCache.get(4); #   // return 4
