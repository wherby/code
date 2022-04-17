from bisect import bisect_right
class Solution:
    def maximumBeauty(self, num, newFlowers: int, target: int, full: int, partial: int):
        cnf =0
        num.sort()
        n = len(num)
        for a in num:
            if a >= target:
                cnf +=1
        pre =[0]*(n)
        for i,a in enumerate(num):
            pre[i] = pre[i-1] +a
        partls =[]
        fullls =[0]
        mn = num[0]
        k = 0
        for i in range(n):
            if mn == num[i]:
                partls.append(k)
                continue
            delta = num[i]-mn
            k += (delta)*i
            mn = num[i]
            partls.append(k)
        k =0
        for i in range(n-1,-1,-1): 
            if num[i]>=target:
                fullls.append(k)
            else:
                k += target- num[i]
                fullls.append(k)
        fullls= fullls
        left,right =0,n-1
        mx = 0
        #print(fullls,num,pre)
        for i in range(cnf,n+1):
            right = i
            t1 = fullls[i]
            if t1>newFlowers:
                break
            remains = newFlowers - t1
            idxL = bisect_right(partls,remains)
            idxL = min(idxL,n-right)
            ti=0
            if idxL !=0:
                ti = (pre[idxL-1] + remains)//(idxL)
                ti =min(target-1,ti)
            #print(ti,pre[idxL-1],idxL,remains,full*right + ti*partial,full*(n-right) + ti*partial, right)
            mx = max(mx, full*right + ti*partial*(right !=n))
            #print(mx,right,ti,idxL,remains,ti,full*right + ti*partial*(right !=n))
        return mx

re = Solution().maximumBeauty([5,5,15,1,9],36,12,9,2)
print(re)
            