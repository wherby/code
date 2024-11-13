

## Segment tree range add lazy marking template error

the code is not correct even works in other solution as algorithm/segmentTree/lazyEval/segmentTreeWithLazySetRangeValueFun.v1.error.py


```python
    def __updateRangeSetValue(self,L,R,l,r,root,value):
        if L <=l<=r<=R:
            #print(R,L,value)
            self.tree[root] =(r-l+1)*value
            self.lazy[root] =True
            self.tracted[root] = value
            return 
        self.__pushDownSetValue(root,l,r)
        mid = (l+r)>>1
        if(mid>=L):
            self.__updateRangeSetValue(L,R,l,mid,2*root+1,value)
        if R>mid:
            self.__updateRangeSetValue(L,R,mid+1,r,2*root+2,value)
        self.__pushUp(root)

```

``` python
    def __update(self,L,R,l,r,root,delta):
        self.__pushDown(root,l,r)
        if r < L or R <l:
            return
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.__pushDown(root,l,r)
            return 
        mid = (l+r) >>1
        if not(l >R or mid<l):
            self.__update(L,R,l,mid,2*root+1,delta)
        if not(mid+1 >R or r <L):
            self.__update(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)
```

or fix with 
```python
    def __update(self,L,R,l,r,root,delta):
        self.__pushDown(root,l,r)
        if r < L or R <l:
            return
        if L <=l <=r<=R:
            self.lazy[root] = True
            self.tracted[root] += delta
            ## need to change
            self.__pushDown(root,l,r)
            return 
        mid = (l+r) >>1
        self.__update(L,R,l,mid,2*root+1,delta)
        self.__update(L,R,mid+1,r,2*root+2,delta)
        self.__pushUp(root)
```