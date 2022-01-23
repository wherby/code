class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        bNSorce = False
        bNTarget = False
        dicVist ={}
        dicBlock ={}
        for a,b in blocked:
            dicBlock[(a,b)] = 1
        def verify(x,y):
            if x >=0 and x < 10**6 and y >=0 and y <10**6 and (x,y) not in dicBlock  and (x,y) not in dicVist:
                return True
            return False
        sst = [source]
        tst =[target]
        while sst:
            a,b = sst.pop()
            dicVist[(a,b)] =1
            if abs(a - source[0]) + abs(b - source[1]) > 200:
                bNSorce = True
                break
            if a == target[0] and b == target[1]:
                return True
            for d1 in dirs:
                if verify(a + d1[0],b+d1[1]):
                    sst.append([a+d1[0],b+d1[1]])
        while tst:
            a,b = tst.pop()
            dicVist[(a,b)] = 1
            if abs(a - target[0]) + abs(b - target[1]) > 200:
                bNTarget = True
                break
            for d1 in dirs:
                if verify(a + d1[0],b +d1[1]):
                    tst.append([a+d1[0],b+d1[1]])
        #print("ccc",bNSorce,bNTarget)
        return bNSorce and bNTarget

re =Solution().isEscapePossible(blocked = [], source = [0,0], target = [999999,999999])
print(re)