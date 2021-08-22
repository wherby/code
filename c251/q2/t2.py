class Solution:
    def maximumNumber(self, num, change):
        res = list([int(i) for i in num])
        start = False
        for i in range(len(res)):
            t = res[i]
            if t < change[t]:
                start  = True
                res[i] = change[t]
            else:
                if start ==True and  t == change[t]:
                    continue
                if start == True:
                    break
        res = list(map(lambda x: str(x),res))
        re = "".join(res)
        res = str(re).rjust(len(num),'0')
        return res


a = Solution().maximumNumber("021", [9,4,3,5,7,2,1,9,0,6])
print(a)
a = Solution().maximumNumber("132",  [9,8,5,0,3,6,4,2,6,8])
print(a)

a = Solution().maximumNumber("334111",  [0,9,2,3,3,2,5,5,5,5])
print(a)
a = Solution().maximumNumber("00000",  [0,3,5,8,7,5,4,6,3,2])
print(a)
a = Solution().maximumNumber("214010",  [6,7,9,7,4,0,3,4,4,7])
print(a)

