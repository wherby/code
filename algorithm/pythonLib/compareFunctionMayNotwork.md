# 

https://stackoverflow.com/questions/79058530/python-sort-lib-different-behavior-with-different-comparing-functions-some-comp

For the comparing function function
```python
from functools import cmp_to_key
def compare(a,b):
    print(a,b, a+b,b+a,a+b>b+a) 
    return (a+b)>(b+a) # first comparing function

def sortArr(ls):
    ls = sorted(ls,key =cmp_to_key(compare),reverse=True)
    return "".join(ls)

ls = ["8","81","82","829"]
print(sortArr(ls))
```

Which will output as:
```
82 829 82829 82982 False
81 82 8182 8281 False
8 81 881 818 True
88182829

```

But using comparing function as:
``` python
from functools import cmp_to_key
def compare(a,b):
    print(a,b, a+b,b+a,a+b>b+a)
    return int(a+b) -int(b+a) # second comparing function

def sortArr(ls):
    ls = sorted(ls,key =cmp_to_key(compare),reverse=True)
    return "".join(ls)

ls = ["8","81","82","829"]
print(sortArr(ls))
```

the output is
```
82 829 82829 82982 False
81 82 8182 8281 False
8 81 881 818 True
8 82 882 828 True
8 829 8829 8298 True
88298281
```


Apparently the second sort function is what's needed. the first function didn't do all comparing use first element.

So why the first comparing function didn't work?


# Answer

https://stackoverflow.com/questions/79058530/python-sort-lib-different-behavior-with-different-comparing-functions-some-comp

It's unclear why you might expect the first function to work. An old-style comparison function has to work like so:

cmp(x, y) is negative if and only if x < y.
cmp(x, y) is 0 if and only if x == y.
cmp(x, y) is strictly positive (> 0) if and only if x > y.
Given that, your return (a+b)>(b+a) doesn't appear to make sense. It can only return True or False, which act like 1 and 0, respectively. So it's impossible for it to return a result which will be interpreted as meaning a is less than b.




``` python 
from functools import cmp_to_key
def compare(a,b):
    if (a+b)==(b+a):return 0
    return 1 if  (a+b)>(b+a) else -1

def sortArr(ls):
    ls = sorted(ls,key =cmp_to_key(compare),reverse=True)
    print(ls)
    return "".join(ls)


ls = ["8","81","82","829"]
print(sortArr(ls))
```