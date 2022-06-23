# KMP match all pattern
# https://www.codespeedy.com/kmp-string-matching-algorithm-in-python/
def getNext(str):
    le = len(str)
    next = [0]*le
    next[0] = 0
    i=0
    j =1
    while j !=le:
        if str[j]  == str[i]:
            i +=1 
            next[j] = i
            j +=1
        elif i !=0:
            i = next[i-1]
        else:
            next[j] =0
            j +=1
    return next

n = getNext("babab")
print(n)


def kmp_string(pattern,text):
    a = len(text)
    b = len(pattern)

    prefix_arr = getNext(pattern)
    print(prefix_arr)
    initial_point =[]

    m = 0
    n = 0
    
    while m != a:
        if text[m] == pattern[n]:
            m +=1
            n +=1
        else:
            n = prefix_arr[n-1]
        if  n == b:
            initial_point.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m +=1
    return initial_point

string = "ABABDABACDABABCABABCABAB"
pat = "ABABCABAB"

initial_index = kmp_string(pat, string)
for i in initial_index:
    print('Pattern is found in the string at index number',i)

s1="abcabcabcabcabc"
n = getNext(s1)
print(n,len(s1))