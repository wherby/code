#https://leetcode.com/problems/lru-cache/

## Python Node list

class Node:
    def __init__(self,key,val):
        self.key =key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self,capacity):
        self.m = {}
        self.capacity = capacity
        self.h = Node(0,0)
        self.t = Node(0,0)
        self.h.next = self.t
        self.t.prev = self.h

    def remove(self, node):
        prev =node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def touch(self,node):
        self.remove(node)
        self.newHead(node)
    
    def newHead(self,node):
        h = self.h.next
        node.next =h 
        h.prev = node
        node.prev = self.h
        self.h.next = node
    
    def get(self,key):
        node = self.m.get(key,None)
        if node:
            self.touch(node)
            return node.val
        return -1

    def put(self,key,val):
        node = self.m.get(key,None)
        if node:
            self.touch(node)
            node.val = val
        else:
            if len(self.m) == self.capacity:
                last = self.t.prev
                self.m.pop(last.key)
                self.remove(last)
            node = Node(key,val)
            self.m[key] = node
            self.newHead(node)

lru = LRUCache(100)

for i in range(100):
    lru.put(i,i)

#print(lru.m)
lru.remove(lru.m[2])
print(lru.m[1].prev.key)

