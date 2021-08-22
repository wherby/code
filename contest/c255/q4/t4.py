class Solution:
    def recoverArray(self, n, sums):
        dic ={}
        for x in sums:
            dic[x] =1
        candidate = []
        for x in sums:
            candidate.append(x)
        tp =[]
        mxC = n*(n-1)/2

        for c in candidate:
            cnt = 0
            for j in sums:
                t = c +j
                if t in dic:
                    cnt +=1

            if cnt >= mxC:
                tp.append(c)
        
        candidate = tp
        tp=[]
        for c in candidate:
            cnt = 0
            for j in sums:
                t = c +j
                if t in dic:
                    cnt +=1

            if cnt >= mxC:
                tp.append(c)
        dic ={}
        

        print(tp)


sums =[0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
re =Solution().recoverArray(4,sums)
