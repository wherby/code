

# stack using python:

```
class Stack:
    """模拟栈"""
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items)==0 
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() 
    
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return 1000000000 #handle empty
        
    def size(self):
        return len(self.items) 
```