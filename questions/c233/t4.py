class node:
    def __init__(self):
        self.right,self.left = None,None
        self.path = 0

class trie:
    def __init__(self,at):
        self.root = node()
        self.at = at
    def insert(self,i):
        curr = self.root
        for j in range(self.at,-1,-1):
            #print(j)
            if not(i&(1<<j)):
                if curr.left == None :
                    curr.left =node()
                curr = curr.left
            else:
                if curr.right ==None:
                    curr.right = node()
                curr =curr.right
            curr.path +=1
    
    def get(self,node):
        if node ==None:
            return 0
        return node.path
    
    def find(self,curr,i,j,at):
        if curr == None:
            return 0
        if at == -1:
            return self.get(curr)
        b,m = i & (1<<at),j&(1<<at)
        if b ==0:
            if m ==0:
                return self.find(curr.left,i,j,at-1)
            else:
                return self.get(curr.left) + self.find(curr.right,i,j,at-1)
        else:
            if m ==0:
                return self.find(curr.right,i,j,at-1)
            else:
                return self.get(curr.right) + self.find(curr.left,i,j,at-1)

class Solution:
    def countPairs(self, nums, low, high) :
        t,ans=trie (len(bin(max (nums+[high+1])))-2),0
        for i in nums:
            ans+=t.find (t.root,i,high,t.at)-t.find (t.root,i,low-1,t.at)
            t.insert (i)
        return ans


nums = [1,4,2,7]
low = 2
high = 6

Solution().countPairs(nums,low,high)