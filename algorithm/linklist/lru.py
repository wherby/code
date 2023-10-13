# https://leetcode.cn/problems/lru-cache/description/?envType=daily-question&envId=2023-09-24

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache ={}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.size = 0 
        self.head.next =self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key,value)
            self.cache[key] = node
            self.addToHead(node)
            self.size +=1
            if self.size > self.capacity:
                remove = self.removeTail()
                del self.cache[remove.key]
                self.size -=1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self,node):
        node.prev = self.head
        node.next = self.head.next 
        self.head.next.prev = node 
        self.head.next = node
    
    def removeNode(self,node):
        node.prev.next = node.next 
        node.next.prev = node.prev
    
    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.prev 
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)