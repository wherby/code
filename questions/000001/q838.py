class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        rls = [0]*n
        lls = [0]*n
        for i,a in enumerate(dominoes):
            if a =="R":
                rls[i] = 0
            elif a == "L":
                rls[i] = n+3
            else:
                if i ==0:
                    rls[0]= n+3
                else:
                    rls[i] = rls[i-1] +1
            b = dominoes[n-i-1]
            if b == "L":
                lls[n-1-i] ==0
            elif b =="R":
                lls[n-1-i] = n+3
            else:
                if i == 0:
                    lls[n-1] = n+3
                else:
                    lls[n-1-i] = lls[n-i]+1
        res = [0]*n
        for i in range(n):
            if min(lls[i],rls[i])> n:
                res[i] ="."
            else:
                if rls[i] > lls[i]:
                    res[i]="L"
                elif rls[i] < lls[i]:
                    res[i] = "R"
                else:
                    res[i] ="."
        return "".join(res)

re = Solution().pushDominoes(".L.R...LR..L..")
print(re)