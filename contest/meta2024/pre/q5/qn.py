#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D2?source=facebook
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



# def resolve():
#     N,G = list(map(lambda x: int(x),input().split()))
#     ls =[]
#     for i in range(N):
#         inp = int(input())
#         ls.append(inp)
#     ret = 0
#     ls.sort()
#     mx = abs(G - ls[0])
#     for i ,a in enumerate(ls):
#         d =abs(G-a)
#         if d <= mx:
#             mx = d 
#             ret = i 

#     return str(N-ret) + " " + str(mx)

# def op(caseidx):
#     cnt = resolve()
#     print("Case #"+str(caseidx+1)+": "+str(cnt))

# for i in range(int(input())):
#     op(i)


#import io,os
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline




def main():
    
    n,g = map(int,input().split())
    arr = []

    for i in range(n):
        x = int(input())
        arr.append(x+i)
    print(arr)
    arr.sort()
    print(arr)

    for i in range(n-2,-1,-1):
        arr[i] -= n - 1 - i
    print(arr)

    

    minimum = 10**18

    ans = -1

    for i in range(n-1,-1,-1):
        index = n - i
        if abs(arr[i]-g) < minimum:
            minimum = abs(arr[i]-g)
            ans = index


   
    print(f"Case #{t}: {ans} {minimum}")        

    




T = int(input())
t = 1
while t <= T:
    main()
    t += 1
