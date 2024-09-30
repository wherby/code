
## 
https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/C/solution?source=facebook

As the queen of an ant colony, it’s your job to ensure that the antire colony works together. Your colony has 
N
N worker ants, the 
i
ith of which is currantly at coordinates 
(
X
i
,
Y
i
)
(X 
i
​
 ,Y 
i
​
 ). To align the efforts of all of your worker ants, you would like them to all be on the same line on the plane. How many of your ants need to move to get them to all lie on the same line?
As is frequantly the case in managemant, you don’t need an exact answer, but you do need some degree of accuracy. If the true minimum number of ants that need to move is 
M
M, then any answer between 
M
M and 
2
∗
M
2∗M (inclusive) will be accepted.
Constraints
1
≤
T
≤
75
1≤T≤75
2
≤
N
≤
1
,
000
,
000
2≤N≤1,000,000
0
≤
∣
X
i
∣
,
∣
Y
i
∣
≤
1
,
000
,
000
,
000
0≤∣X 
i
​
 ∣,∣Y 
i
​
 ∣≤1,000,000,000
In each test case, no two ants will be at the same position.
The sum of 
N
N across all test cases is at most 
4
,
000
,
000
4,000,000.
Input Format
Input begins with an integer 
T
T, the number of test cases. Each case starts with a line that contains the integer 
N
N. Then 
N
N lines follow, the 
i
ith of which contains the integers 
X
i
X 
i
​
  and 
Y
i
Y 
i
​
 .
Output Format
For the 
i
ith test case, print "Case #i: " followed by the number of ants you need to move to get all of the ants to lie on the same line.
Sample Explanation
In the first case, the 
4
4 ants are all on the line 
y
=
x
y=x, so no ants need to be moved. 
0
0 is the only answer that will be accepted for this case.
In the second case, the 
4
4 ants are at the vertices of a square, so every line contains at most 
2
2 of the 
4
4 ants. 
2
2 ants need to be moved, so the answers 
2
2, 
3
3, and 
4
4 will be accepted for this case.
The third case is depicted below. Ants 
2
2, 
4
4, 
5
5, and 
7
7 all lie on the line 
y
=
3
2
x
+
1
y= 
2
3
​
 x+1. Moving the other 
3
3 ants is the optimal way to get all of the ants on a single line, so any answer between 
3
3 and 
6
6 inclusive will be accepted for this case.



##

Since 
N
N is up to a million, it will be too slow to construct lines from all 
O
(
N
2
)
O(N 
2
 ) pairs of ants.
Let 
P
P be the number of ants on the optimal line (i.e. the line with most ants, requiring the minimum number of ants to be moved). Then, the answer needs to be between 
M
=
N
−
P
M=N−P
 and 
2
M
=
2
(
N
−
P
)
=
N
−
(
2
P
−
N
)
.
2M=2(N−P)=N−(2P−N).
These bounds indicate that we need to find a line containing between 
2
P
−
N
2P−N and 
P
P ants.
Consider this probabilistic algorithm that runs in 
O
(
K
N
)
O(KN) time, where 
K
K is the number of trials:
Randomly choose 
2
2 ants, independently and uniformly. Construct a line going through them.
Check how many ants lie on this line in 
O
(
N
)
O(N) time.
Repeat 
K
K times, and return the line with the most ants across all trials.
If 
P
≤
N
2
P≤ 
2
N
​
 , then 
2
P
−
N
≤
2
N
2
−
N
=
0
2P−N≤2 
2
N
​
 −N=0. So, simply choosing any line containing 
2
2 ants will be sufficient, as 
2
2 falls within 
[
0
,
P
]
⊆
[
2
P
−
N
,
P
]
[0,P]⊆[2P−N,P].
If 
P
>
N
2
P> 
2
N
​
 , then the probability that 
2
2 uniformly randomly chosen ants are not both on the optimal line is less than 
0.75
0.75. Thus, the probability that the optimal line is not found over any of the 
K
K trials is less than 
(
0.75
)
K
(0.75) 
K
  which is around 
0.001
%
0.001% for only 
K
=
40
K=40 trials.
In either case, the algorithm will find a satisfactory line containing some 
p
p ants, for which we can return a final answer of 
N
−
p
N−p.