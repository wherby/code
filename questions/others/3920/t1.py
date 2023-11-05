class Solution:
    def valid(self,preord, index):
        if index >=len(preord):
            self.isvalid = False
            return 10**9
        if  preord[index]=='#':
            return index +1
        rightIndex = self.valid(preord,index +1)
        if rightIndex >= len(preord):
            self.isvalid = False
        endIndex = self.valid(preord,rightIndex)
        return endIndex

    def isValidSerialization(self, preorder):
        preorder=preorder.split(",")
        self.isvalid = True
        right =self.valid(preorder,0)
        #print(right,len(preorder))
        if right != len(preorder):
            self.isvalid =False
        return self.isvalid

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
re=Solution().isValidSerialization(preorder)
print(re)