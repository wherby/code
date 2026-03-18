

## Sqrt related 

求 x*(x+1) <= n 求x 
这里用到
···
t = mid // a * 2
p = int(math.sqrt(t))
if p*(p+1) <=t:
    acc +=p
else:
    acc += max(0,p-1)
···
计算， 也可以直接用 4个p*(p+1)的长方形 加上中间的1 构成 （p*2+1)的正方形
···
t= mid //a *2
p =(int(math.sqrt(t*4+1)) -1)//2
···
```python
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        l,r = 0 ,10**20 
        def verify(mid):
            acc = 0 
            for a in workerTimes:
                t = mid // a * 2
                p = int(math.sqrt(t))
                if p*(p+1) <=t:
                    acc +=p
                else:
                    acc += max(0,p-1)
            return acc >= mountainHeight

        while l <r :
            mid = (l+r)>>1
            if verify(mid):
                r= mid 
            else:
                l = mid +1
        return l
```