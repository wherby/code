# use node in segment_tree
from math import ceil, log2

class Node:
    def __init__(self,val):
        self.val = val
        self.maxL = 1
        self.leftC=val
        self.rightC =val
        self.leftN = 1
        self.rightN =1
        self.size = 1
    def __str__(self):
        #print(vars(self))
        # for key,value in self.__dict__.iteritems():
        #     print(key,value)
        return 'Node ['+str(vars(self)) +']'

def mergeNode(nodeA,nodeB): 
    node = Node(nodeA.leftC)
    node.leftC = nodeA.leftC
    node.rightC = nodeB.rightC
    node.leftN = nodeA.leftN
    node.rightN = nodeB.rightN
    node.size = nodeA.size + nodeB.size
    node.maxL = max(nodeA.maxL,nodeB.maxL)
    if nodeA.rightC == nodeB.leftC:
        merged = nodeA.rightN + nodeB.leftN
        node.maxL = max(node.maxL,merged)
        if nodeA.rightN == nodeA.size:
            node.leftN = merged
        if nodeB.leftN == nodeB.size:
            node.rightN = merged
    return node

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basef=lambda x:x, basev = 0):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v         
class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        sls = [a for a in s]
        segTree = segment_tree(sls,lambda x,y :mergeNode(x,y),lambda x:Node(x),lambda x:Node("1"))
        res =[]
        for i,a in enumerate(queryIndices):
            segTree.update(a,queryCharacters[i])
            res.append(segTree.tree[0].maxL)
        return res

re =Solution().longestRepeating(s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3])
print(re)