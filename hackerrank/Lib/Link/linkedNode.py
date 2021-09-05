class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def addList(self,listAnother):
        self.last.next = listAnother.first
        self.last = listAnother.last

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

L = LinkedList()
L.insert(1)
L.insert(1)
L.insert(2)
L.insert(4)

L2 = LinkedList()

L2.insert(11)
L.addList(L2)
L2.insert(11)
L2.insert(22)
L2.insert(42)

print L
print L2
L.clear()
print L