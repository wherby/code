class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        inventory.sort()
        l = 0
        r = inventory[-1]
        n =len(inventory)
        def getNum(mid):
            cnt =0
            for i in inventory:
                if i > mid:
                    cnt += i-mid
            return cnt 
        while l<r:
            mid = (l+r) >>1
            cnt = getNum(mid)
            if cnt <orders:
                r = mid
            else:
                l = mid+1
        ls = [0]*n
        acc= 0
        for i in range(n):
            if inventory[i] > l:
                acc += inventory[i] -l
                ls[i] =inventory[i] -l
        remains = orders -acc
        for i in range(n-remains,n):
            ls[i] +=1
        retv= 0
        for i in range(n):
            k = inventory[i] - ls[i]
            retv += (k+ inventory[i]+1) * ls[i] //2
        #print(ls,inventory)
        mod = 10**9+7
        return retv % mod