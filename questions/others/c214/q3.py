class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        inventory.sort(reverse= True)
        max_profit = 0
        mod= 10**9 +7
        curMax, cur_pv = inventory[0],1
        i = 1
        while i< len(inventory):
            cur_delta =curMax - inventory[i]
            if cur_delta >0:
                if orders >= cur_delta * cur_pv:
                    orders -=cur_delta * cur_pv
                    max_profit  += cur_pv *((curMax +inventory[i]+1)*cur_delta//2)
                else:
                    cen = orders // cur_pv
                    max_profit += cur_pv *((curMax + curMax -cen +1) *cen //2)
                    max_profit += (orders% cur_pv) *(curMax -cen)
                    return max_profit %mod
            curMax = inventory[i]
            cur_pv +=1
            i +=1
        if orders >0:
            cen = orders // cur_pv
            max_profit += cur_pv * ((curMax + curMax -cen +1)* cen //2)
            max_profit += (orders %cur_pv) *(curMax -cen)
        return max_profit %mod

re = Solution().maxProfit(inventory = [2,5], orders = 4)
print(re)