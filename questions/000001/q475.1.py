class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.append(-10**19)
        heaters.append(10 **19)
        heaters.sort()
        n1,n2 = len(houses),len(heaters)
        ans = 0
        i,j = 0,1
        while i < n1 and j <n2:
            if houses[i] == heaters[j]:
                i +=1
                j +=1
            elif houses[i] < heaters[j]:
                ans  = max(ans, min(heaters[j] -houses[i],houses[i]-heaters[j-1]))
                i+=1
            else:
                j +=1
        return ans


re = Solution().findRadius([1,5],[10])
print(re)