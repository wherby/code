filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
from bisect import bisect_left, bisect_right
import bisect
import operator

class SortedCollection(object):
    def __init__(self, iterable=(), key=None):
        self._given_key = key
        key = (lambda x: x) if key is None else key
        decorated = sorted((key(item), item) for item in iterable)
        self._keys = [k for k, item in decorated]
        self._items = [item for k, item in decorated]
        self._key = key

    def _getkey(self):
        return self._key

    def _setkey(self, key):
        if key is not self._key:
            self.__init__(self._items, key=key)

    def _delkey(self):
        self._setkey(None)

    key = property(_getkey, _setkey, _delkey, 'key function')

    def clear(self):
        self.__init__([], self._key)

    def copy(self):
        return self.__class__(self, self._key)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, i):
        return self._items[i]

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __repr__(self):
        return '%s(%r, key=%s)' % (
            self.__class__.__name__,
            self._items,
            getattr(self._given_key, '__name__', repr(self._given_key))
        )

    def __reduce__(self):
        return self.__class__, (self._items, self._given_key)

    def __contains__(self, item):
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return item in self._items[i:j]

    def index(self, item):
        'Find the position of an item.  Raise ValueError if not found.'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return self._items[i:j].index(item) + i

    def count(self, item):
        'Return number of occurrences of item'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return self._items[i:j].count(item)

    def insert(self, item):
        'Insert a new item.  If equal keys are found, add to the left'
        k = self._key(item)
        i = bisect_left(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)

    def insert_right(self, item):
        'Insert a new item.  If equal keys are found, add to the right'
        k = self._key(item)
        i = bisect_right(self._keys, k)
        self._keys.insert(i, k)
        self._items.insert(i, item)

    def remove(self, item):
        'Remove first occurence of item.  Raise ValueError if not found'
        i = self.index(item)
        del self._keys[i]
        del self._items[i]

    def find(self, k):
        'Return first item with a key == k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i != len(self) and self._keys[i] == k:
            return self._items[i]
        raise ValueError('No item found with key equal to: %r' % (k,))

    def find_le(self, k):
        'Return last item with a key <= k.  Raise ValueError if not found.'
        i = bisect_right(self._keys, k)
        if i:
            return self._items[i-1]
        raise ValueError('No item found with key at or below: %r' % (k,))

    def find_lt(self, k):
        'Return last item with a key < k.  Raise ValueError if not found.'
        i = bisect_left(self._keys, k)
        if i:
            return self._items[i-1]
        raise ValueError('No item found with key below: %r' % (k,))

    def find_ge(self, k):
        'Return first item with a key >= equal to k.  Raise ValueError if not found'
        i = bisect_left(self._keys, k)
        if i != len(self):
            return self._items[i]
        raise ValueError('No item found with key at or above: %r' % (k,))

    def find_gt(self, k):
        'Return first item with a key > k.  Raise ValueError if not found'
        i = bisect_right(self._keys, k)
        if i != len(self):
            return self._items[i]
        raise ValueError('No item found with key above: %r' % (k,))

sortedList = SortedCollection(key=operator.itemgetter(1))

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

class KeyifyList(object):
    def __init__(self, inner, key):
        self.inner = inner
        self.key = key

    def __len__(self):
        return len(self.inner)

    def __getitem__(self, k):
        return self.key(self.inner[k])


n, = map(int , ins[0].strip().split())
ls =  map(int , ins[1].strip().split())
ring= [0]
dis =0
for i in ls:
    ring.append(dis)
    dis = dis +i
ring.append(dis)
nodes = []
for i in range(n +1):
    nodes.append([0,[]])
dic1={}
nodeOrd =[]

def addNodeOrd(node):
    global nodeOrd,sortedList
    sortedList.insert(node)

def removeNodeOrd(node):
    global nodeOrd,sortedList
    try:
        sortedList.remove(node)
    except:
        pass


def getBase(x1,x2):
    global ring,n
    if x1==x2:
        return 0
    if x2>x1:
        return ring[x2]-ring[x1]
    else:
        return ring[n+1]-ring[x1] + ring[x2]

def getTotalDis(x1,x2):
    global nodes
    return getBase(x1,x2) + nodes[x2][0]


def findFarest(x1):
    global nodes,n, dic1 ,nodeOrd,ring, sortedList
    if x1==1:
        farNode =n
    else:
        farNode = x1 -1
    farWT = getTotalDis(x1,farNode)     
    if len(sortedList) > 0:
        maxOrdNode = sortedList[-1]
        diffs = maxOrdNode[1] - ring[-1] + getBase(x1,maxOrdNode[0])
        i = bisect_left(sortedList._keys, diffs)
        for key,value in sortedList[i:]:
            tmp = getTotalDis(x1,key)
            if tmp > farWT:
                farWT =tmp
                farNode =key
    return (farNode,farWT)


def addToNode(x,w):
    global nodes,dic1,nodeOrd
    removeNodeOrd([x,nodes[x][0]])
    i= bisect.bisect_left(KeyifyList(nodes[x][1],lambda x:x[0]),w)
    nodes[x][1]= nodes[x][1][:i] +[[w,[w]]] +nodes[x][1][i:]
    if nodes[x][0]<w:
        nodes[x][0] = w
    addNodeOrd([x,nodes[x][0]])
    dic1[x] =1


def addToMaxNode(x,w):
    global nodes,dic1
    removeNodeOrd([x,nodes[x][0]])
    dic1[x] =1
    if len(nodes[x][1]) ==0:
        nodes[x][1].append([w,[w]])
        nodes[x][0] =w
    else:
        nodes[x][1][-1][1].append(w)
        nodes[x][1][-1][0] = nodes[x][1][-1][0] +w
        nodes[x][0] = nodes[x][0] +w
    addNodeOrd([x,nodes[x][0]])


def removeFromNode(x):
    global nodes,dic1
    removeNodeOrd([x,nodes[x][0]])
    node = nodes[x][1].pop()
    y = node[1].pop()
    node[0] = node[0] -y
    if node[0] != 0:
        i= bisect.bisect_left(KeyifyList(nodes[x][1],lambda x:x[0]),node[0])
        nodes[x][1]= nodes[x][1][:i] +[node] +nodes[x][1][i:]
    if len(nodes[x][1]) ==0:
        nodes[x][0] =0
        del dic1[x]
    else:
        nodes[x][0] = nodes[x][1][-1][0]

    if nodes[x][0] != 0:
        addNodeOrd([x,nodes[x][0]])




def addToFar(x,w):
    farNode,farWT =findFarest(x)
    addToMaxNode(farNode,w)

def removeFromFar(x):
    farNode,farWT =findFarest(x)
    removeFromNode(farNode)

def printFarV(x):
    farNode,farWT =findFarest(x)
    print(farWT)


q, = map(int , ins[2].strip().split())
index=3
for i in range(q):
    tp=list(map(int , ins[index+i].strip().split()))
    if tp[0] == 1:
        x1,x2,w1 = tp
        addToFar(x2,w1)
    if tp[0]==2:
        x1,x2,w1 = tp
        addToNode(x2,w1)
    if tp[0] ==3:
        x1,x2 =tp
        removeFromFar(x2)
    if tp[0] ==4:
        x1,x2 = tp
        printFarV(x2)

    #print dic1,"  xxx  ",nodeOrd, "   YYY   ",tp, "   xxx      ",nodes



print nodes
print dic1
print nodeOrd
print sortedList