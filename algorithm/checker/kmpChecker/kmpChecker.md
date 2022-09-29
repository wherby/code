# KMP checker

Using the algorith code for question https://leetcode.cn/problems/string-rotation-lcci/submissions/
find the input 
```
"aba"
"bab"
```
can't work.

```
#https://www.codespeedy.com/kmp-string-matching-algorithm-in-python/ 
def KMP_String(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
    print(prefix_arr)
    initial_point = []
    m = 0
    n = 0
  
    while m != a:
        print(m,n,a,b)   
        if text[m] == pattern[n]:
            m += 1
            n += 1

        else:
            n = prefix_arr[n-1]
        print("aa",m,n,a,b) 
        if n == b:
            print(m,b,n,text,pattern,n)
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1
   
    return initial_point
def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
                n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    #print(prefix_arr)
    return prefix_arr


string = "abaaba"
pat = "bab"
initial_index = KMP_String(pat,string)
print(initial_index)
```

The output is as:
```
[0, 0, 1]
0 0 6 3
aa 0 1 6 3
0 1 6 3
aa 1 2 6 3
1 2 6 3
aa 2 3 6 3
2 3 3 abaaba bab 3
2 1 6 3
aa 3 2 6 3
3 2 6 3
aa 3 0 6 3
4 0 6 3
aa 5 1 6 3
5 1 6 3
aa 6 2 6 3
[-1]
```

Which means the KMP algorith has bug,

```
        if text[m] == pattern[n]:
            m += 1
            n += 1
      
        else:
            n = prefix_arr[n-1]  ## n could be 0, then n-1 is -1
       
        if n == b:
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1
```

