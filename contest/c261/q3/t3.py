class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        sm= sum(stones)
        st =[0]*n
        for i in range(n):
            st[i] = stones[i] %3
        cnt = [0]*3
        for s in st:
            cnt[s] +=1
        move = cnt[0]
        mxMov = [0,False]
        #print(cnt)
        def dfs(idx,mv,s1,s2):
            t = idx %3
            if t ==1 and s1 == cnt[1]:
                mxMov[0] = max(mxMov[0],mv)
                return mv
            if t ==1:
                #print("m1",idx)
                mv1 = dfs(idx + 1 ,mv+1,s1 +1 ,s2)
                mxMov[0] = max(mxMov[0],mv1)
                return mv1
            if t ==2 and s2  == cnt[2]:
                mxMov[0]= max(mxMov[0],mv)
                return mv
            if t ==2:
                #print("m2",idx)
                mv2 = dfs(idx +2,mv +1,s1,s2+1)
                mxMov[0] = max(mxMov[0],mv2)
                return mv2
            mv3 =mv4 =0
            if t ==0 and s1 < cnt[1]:
                #print("m1",idx)
                mv3 = dfs(idx +1,mv +1,s1+1,s2)
                
            if t ==0 and s2 < cnt[2]:
                #print("m2",idx)
                mv4 = dfs(idx +2,mv +1,s1,s2+1)
            if (mv3-mv4) %2 !=0 and mv3 *mv4 >0:
                print(mv3,mv4)
                mxMov[1] = True
            return max(mv4,mv3)
        move2 = dfs(0,0,0,0)


        allMov =0
        if move2 >0:
            if move %2 ==1:
                return False
            allMov = move + move2
        if mxMov[1] == True:
            return True
        if allMov == n :
            return False
        print(allMov)

        if allMov %2 ==1:
            return True

        return False
        

re = Solution().stoneGameIX( [19,2,17,20,7,17])
print(re) #[1,2,2,2,1,2]
print(re ,True)

re = Solution().stoneGameIX( [3])
print(re)

re = Solution().stoneGameIX( [2])
print(re)

re = Solution().stoneGameIX([15,20,10,13,14,15,5,2,3])
print(re) #[2,1,1,2,2,2]
print(re ,False)
