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

class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ls =LinkedList()
        for i,a in enumerate(nums):
            ls.append(i,a)
        cand=[]
        for i in range(n-1,0,-1):
            if nums[i-1]> nums[i]:
                cand.append(i)
        turn =0
        dic ={}
        #print(cand,ls.m)
        while cand:
            turn +=1
            nex=[]
            for a in cand:
                if a not in dic:
                    dic[a] =1
                    nn = ls.m[a]
                    nleft = nn.prev.key
                    nright =nn.next.key
                    ls.removeByKey(a)
                    #print(nleft,nright)
                    if nleft>=0 and nright >=0 and   nums[nleft] > nums[nright]:
                        nex.append(nright)
            cand =nex
        #print(turn)
        return turn 
                

#re= Solution().totalSteps([10,6,5,10,3])
t2= [82,228,317,559,670,1535,1977,890,1243,1502,1720,1808,1819,1966,105,170,194,320,385,433,607,633,1144,1195,1365,1490,1778,921,1560,6,68,69,100,341,595,679,725,775,887,1316,296,613,658,682,777,1203,1350,1431,161,374,784,794,863,1080,1149,1509,1525,128,437,996,1045,1061,1102,1238,1624,1706,1961,808,950,1166,1531,1537,1732,866,1279,1494,1527,1595]
#re= Solution().totalSteps([7,11,1])
re = Solution().totalSteps(t2)
print(re)            