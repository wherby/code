n,a,b = tuple(list(map(lambda x: int(x),input().split())))




## return

```python
    ret= resolve()
    ret = list(map(lambda x:str(x),ret))
    if len(ret) ==0:
        print("Case #"+str(caseidx+1)+": " + "IMPOSSIBLE")
    else:
        print("Case #"+str(caseidx+1)+": " + "POSSIBLE")
        print(str(len(ret)))
        print(" ".join(ret))
```

## return div number

    for i in range(a*b):
        if (i*mod +a) %b ==0:
            return (i*mod+a)//b