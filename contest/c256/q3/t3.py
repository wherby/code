class Solution:
    def testx(self,mask, tasks,turn,res,sessionTime,k):
        #print("aa")
        # print(k,mask)
        # self.u +=1
        # if self.u > 100:
        #     return
        n = len(tasks)
        if k ==n and self.dp[mask] == turn *sessionTime + res :
            return
        if k ==n :
            return
            k=k%n
            turn +=1
        if self.dp[mask] < turn *sessionTime + res :
            return 0
        i=k
        #print("aa",mask,(mask & k<<i),(mask & k<<i) ==0)
        if  (mask & k<<i) ==0:
            #print("cc")
            if tasks[i] +res > sessionTime:
                #print("dd")
                self.testx(mask | 1<<i, tasks,turn +1, tasks[i],sessionTime,k+1)
                self.dp[mask | 1<<i] =min( self.dp[mask | 1<<i], (turn+1)* sessionTime + tasks[i])
            else:
                #print("ee",i,mask | 1<<i)
                self.testx(mask| 1<<i,tasks, turn ,  tasks[i] + res,sessionTime,k+1)
                self.dp[mask | 1<<i] =min( self.dp[mask | 1<<i], (turn)* sessionTime + tasks[i] + res)
            self.testx(mask,tasks,turn, res,sessionTime,k+1)

    def minSessions(self, tasks, sessionTime) :
        self.u =0
        n = len(tasks)
        self.dp = [100000000] * (2 <<n)
        self.dp[0]=0
        self.testx(0,tasks,0,0,sessionTime,0)
        #print(self.dp[:32])
        #print(self.dp[2<<n-1],(2<<n-1)-1,n)
        return (self.dp[(2<<n-1)-1] +sessionTime -1 )//sessionTime

tasks = [1,2,3]
re = Solution().minSessions(tasks,3)
print(re)

