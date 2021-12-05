class Solution(object):
    
    def getDirections(self, root, startValue, destValue):
        def getPath(ele,value,path):
            if ele.val == value:
                return True
            if ele.left and getPath(ele.left,value,path):
                path.append("L")
                return True
            elif ele.right and getPath(ele.right,value, path):
                path.append("R")
                return True
            return False
        sp,dp =[],[]
        getPath(root,startValue,sp)
        getPath(root,destValue,dp)
        while sp and dp and sp[-1] ==dp[-1]:
            sp.pop()
            dp.pop()
        return "".join(["U"]*len(sp)+dp[::-1])