# Enter your code here. Read input from STDIN. Print output to STDOUTimport sys


n = int(raw_input().strip())
ins=[]
for i in range(2):
    tmp= map(int,raw_input().strip().split(' '))
    tmp.sort()
    ins.append(tmp)
a = sum(ins[0])
b = sum(ins[1])

if a!= b:
    print -1
else:
    c = [ins[0][i]-ins[1][i] for i in range(len(ins[0]))]
    d=filter(lambda x: x>0,c)
    print sum(d)





Your submission will run against only preliminary test cases. Full test cases will run at the end of the day.
Consider two -element multisets (i.e., unordered and possibly containing duplicate elements) of integers,  and . You can perform the following operation on set :

Choose two elements at some postions  and  where  and .
Decrement  by  and increment  by .
Given  and , find and print the minimum number of operations you must perform so that  is equal to  (i.e., both sets contain the same exact values, and the order doesn't matter); if such a thing is not possible, print  instead.

Input Format

The first line contains a single integer, . 
The second line contains  space-separated integers describing the respective values of set . 
The third line contains  space-separated integers describing the respective values of set .

Constraints

, where .
 for at least  of the test cases.
Output Format

Print a single integer denoting the minimum number of operations required to make set  equal to set ; if no number of operations will ever make the two sets equal, print  instead.

Sample Input 0

3
1 2 3
-1 4 3
Sample Output 0

2
Explanation 0 
In this example, we perform two operations:

Sample Input 1

3
1 2 3
2 3 2
Sample Output 1

-1
Explanation 1 
Because no amount of operations will result in sets  and  being equal, we print .