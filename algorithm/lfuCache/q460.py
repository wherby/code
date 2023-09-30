# https://leetcode.cn/problems/lfu-cache/
# https://leetcode.cn/problems/lfu-cache/solutions/2457716/tu-jie-yi-zhang-tu-miao-dong-lfupythonja-f56h/?envType=daily-question&envId=2023-09-25
from collections import defaultdict,deque

class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None 
        self.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.dic={}
        self.capacity = capacity
        def new_list():
            dummy = Node()
            dummy.prev = dummy
            dummy.next = dummy
            return dummy
        self.freq_to_dummy  = defaultdict(new_list)
        self.min_freq = 0
            
            
    def remove(self,x:None):
        x.prev.next = x.next 
        x.next.prev = x.prev
    
    def push_front(self,dummy, x):
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x 
        x.next.prev = x

    def get_node(self, key: int) ->Node:
        if key not in self.dic:
            return None
        node = self.dic[key]
        self.remove(node)
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:
            del self.freq_to_dummy[node.freq]
            if self.min_freq == node.freq:
                self.min_freq +=1
        node.freq +=1
        self.push_front(self.freq_to_dummy[node.freq],node)
        return node
    
    def get(self,key):
        node = self.get_node(key)
        #print(node,self.dic)
        return node.value if node else -1
    
    def put(self,key,value):
        node =self.get_node(key)
        #print(self.dic, key,value)
        if node:
            node.value = value
            return
        if len(self.dic) == self.capacity:
            dummy = self.freq_to_dummy[self.min_freq]
            back_node = dummy.prev
            del self.dic[back_node.key]
            self.remove(back_node)
            if dummy.prev == dummy:
                del self.freq_to_dummy[self.min_freq]
        self.dic[key] = node = Node(key,value)
        self.push_front(self.freq_to_dummy[1],node)
        self.min_freq =1

        