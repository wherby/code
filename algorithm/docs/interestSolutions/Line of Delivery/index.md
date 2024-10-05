
# Question

https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D2?source=facebook



And the solution is  contest/meta2024/pre/q5/qn.py from Xu hao https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/scoreboard?source=facebook

The solution is insane...


``` python 
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

```



Problem D2: Line of Delivery (Part 2)
40 points

Validate Solution & Submit
Problem
My Submissions
Solution
This problem shares some similarities with problem D1, with key differences in bold.
Candice is playing a solitaire game of curling on a 
1
1-dimensional sheet of ice, using stones that are 
1
1 unit wide. She will throw 
N
N stones (numbered 
1
1 to 
N
N) from position 
0
0, targeting a position 
G
G units to the right. In curling, though we say a stone is “thrown”, it’s actually slid along the ice.
The 
i
ith stone will be thrown with energy 
E
i
E 
i
​
 , and will travel 
E
i
E 
i
​
  units to the right unless it collides with another stone, in which case it will transfer its remaining energy to the stone it hits. Formally, we repeat this process until all stones are stationary:
If the moving stone is at position 
p
p and there is a stationary stone at position 
p
+
1
p+1, the moving stone stops at position 
p
p, and the stone at position 
p
+
1
p+1 is now the moving stone with the remaining energy of the previous moving stone.
Otherwise, the moving stone moves 
1
1 unit to the right and its energy is reduced by 
1
1. If the moving stone now has energy 
0
0, it becomes stationary.
After all of the stones are thrown, which stone is closest to the goal position 
G
G, and how far away from the goal is it?
Constraints
1
≤
T
≤
80
1≤T≤80
1
≤
N
≤
300
,
000
1≤N≤300,000
1
≤
G
≤
1
,
000
,
000
1≤G≤1,000,000
N
≤
E
i
≤
1
,
000
,
000
N≤E 
i
​
 ≤1,000,000
All stones are thrown with energy 
E
i
≥
N
E 
i
​
 ≥N, so that stones do not pile up near Candice, but the energies are not necessarily unique.
The sum of 
N
N across all test cases is at most 
2
,
000
,
000
2,000,000.
Input Format
Input begins with an integer 
T
T, the number of test cases. Each case starts with a line that contains the integers 
N
N and 
G
G. Then 
N
N lines follow, the 
i
ith of which contains 
E
i
E 
i
​
 .
Output Format
For the 
i
ith test case, print "Case #i: " followed by the index of the stone that ends up closest to the goal, 
G
G, and how far away it is from 
G
G. If there’s a tie, output the stone with the lowest index.
Sample Explanation
The third sample case is depicted below. The first stone stops at position 
8
8, and the second stone stops at position 
7
7. The third stone starts with an energy of 
9
9, but stops at position 
6
6, transferring 
3
3 energy to the second stone. The second stone is already touching the first stone, so it transfers 
3
3 energy to the first stone, which then moves to position 
11
11. The fourth stone starts with energy 
6
6, and stops at position 
5
5, transferring 
1
1 energy to the next stone, which again transfers 
1
1 energy to the next stone, which then moves to position 
8
8. so the final positions of the stones are 
[
11
,
8
,
6
,
5
]
[11,8,6,5] with stone 
2
2 being at position 
8
8, the goal.