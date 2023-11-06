
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        n = len(root)
        res=[]
        def getRevers(dir):
            if dir =="L":
                return "UL"
            if dir =="R":
                return "UR"
            if dir =="UL":
                return "L"
            if dir == "UR":
                return "R"
        recordV=[]
        finish = False
        def dfs(seed):
            nonlocal finish,res
            t,dir = seed
            x = root[t]
            if x == None:
                return
            print(recordV,finish,x,res)
            if len(recordV) >0 and finish == False:
                res.append((dir))
            if x==startValue or x == destValue:
                if len(recordV)>0:
                    if recordV[0] ==x:
                        res=[]
                    else:
                        finish = True
                recordV.append(x)
            
            if t*2+1 <n:
                dfs((t*2+1,"L"))
            if x==startValue or x == destValue:
                if len(recordV)>0:
                    if recordV[0] ==x:
                        res=[]
            if t*2 +2< n:
                dfs((t*2 +2,"R"))
            if len(recordV) >0 and finish == False:
                res.append((getRevers(dir)))
           
        x = root[0]
        if x==startValue or x == destValue:
                if len(recordV)>0:
                    if recordV[0] ==x:
                        res=[]
                    else:
                        finish = True
                recordV.append(x)
        dfs((0,"L"))
        cres=[]
        #print(res)
        find = 0
        revers=False
        if recordV[0] == destValue:
            revers = True
      
        if revers == False:
            for x in res:
                if len(x)==1:
                    cres.append(x)
                else:
                    cres.append(x[0])
        else:
            for x in reversed(res):
                rx = getRevers(x)
                if len(rx) ==1:
                    cres.append(rx)
                else:
                    cres.append(rx[0])
                    
        return "".join(cres)
        

        
            


re = Solution().getDirections(root =[7,8,3,1,None,4,5,6,None,None,None,None,None,None,2], startValue = 7, destValue = 5)
print(re)