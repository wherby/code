class Solution(object):
    def countCombinations(self, pieces, positions):
        """
        :type pieces: List[str]
        :type positions: List[List[int]]
        :rtype: int
        """
        xymovs =[]
        xandymovs =[]
        for i in range(1,8):
            xymovs.append([i,0])
            xymovs.append([-i,0])
            xymovs.append([0,i])
            xymovs.append([0,-i])
            xandymovs.append([i,i])
            xandymovs.append([i,-i])
            xandymovs.append([-i,i])
            xandymovs.append([-i,-i])
        qmovs = xymovs +xandymovs
        def getMoves(pos,patten):
            x,y = pos
            res =[]
            for m in patten:
                x1 = m[0] +x
                y1= m[1] +y
                if x1 >=1 and x1 <=8 and y1 >=1 and y1<=8:
                    res.append([x1,y1])
            return res
        n = len(pieces)
        moves=[]
        for i in  range(n):
            p = pieces[i]
            pos = positions[i]
            mt =[]
            if p == "rook":
                mt=getMoves(pos,xymovs+[[0,0]])
            if p =="queen":
                mt =getMoves(pos,qmovs+[[0,0]])
            if p =="bishop":
                mt = getMoves(pos,xandymovs+[[0,0]])
            moves.append(mt)
        cnt =0
    
        s =1
        dic ={}
        #print(moves)
        cnt2 = 0
        dic2={}
        for mv in moves:
            dic ={}
            for m1 in mv:
                k = m1[0]*8+ m1[1]
                if k  in dic2:
                    cnt2 +=1
                dic[k] = s
                dic2[k] =1
            s = len(dic) *s
        cnt = 0
        for k,v in dic.items():
            cnt += v
        print(cnt,cnt2)
        return cnt -cnt2
pieces = ["queen","bishop"]
positions = [[5,7],[3,4]]
re = Solution().countCombinations(pieces,positions)
print(re)