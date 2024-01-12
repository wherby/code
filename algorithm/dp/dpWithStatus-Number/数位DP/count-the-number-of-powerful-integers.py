# https://leetcode.cn/problems/count-the-number-of-powerful-integers/
from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        kt = 10**len(s)
        @cache
        def f(i,is_limit,is_num,ss):
            if is_num == False and len(ss) -i < len(s):
                return 0 
            if i ==len(ss) :
                return is_num and int(ss) >= int(s)
            res =0
            if not is_num:
                res = f(i+1,False,False,ss) ##计算 0-9，10-99，100-999，1000-9999
            up = min(limit, int(ss[i])) if is_limit else limit
            if i < len(ss) -len(s):
                for d in range(0 if is_num else 1, up +1):
                    res += f(i+1 ,is_limit  and d ==int(ss[i]) , True,ss)
            else:
                ki = i -(len(ss) - len(s))
                if is_limit:
                    if int(s[ki]) in range(0,up+1):
                        res += f(i+1,is_limit  and s[ki]==ss[i],True,ss)
                    else:
                        #print("II")
                        return 0 
                else:
                    res +=1

            return res
        
        return f(0,True,False,str(finish)) - f(0,True,False,str(start-1))


re = Solution().numberOfPowerfulInt(start = 1, finish = 971, limit = 9, s = "72")
print(re)


# Gd ={"a":1,"b":3,"e":2,"t":2}
# Cd ={"a":2,"e":5} 

# def getItemForCompany(item):
#     ret = Gd.get(item)
#     ret = Cd.get(item, ret)
#     return ret 

# # print(getItemForCompany("a"))
# # print(getItemForCompany("b"))

# def getItems(items,dic):
#     return {a:dic[a] for a in items if a in dic}

# print(getItems(["a","b","e"], Gd))
# print(getItems(["a","b","e"], Cd))
# qs= ["a","b","e"]

# res = {}
# for k,v in getItems(["a","b","e"], Gd).items():
#     res[k] = v 

# for k,v in getItems(["a","b","e"], Cd).items():
#     res[k] = v 

# print(res)


