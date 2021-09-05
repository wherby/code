# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys,math
sta=1465920000.0 + 28800.0
end=1468512000.0 + 28800.0

ins=[]
for line in sys.stdin:
    ins.append(line)

n,m=map(int,ins[0].split())

tps=[]
def getTime(it):
    if it>=sta and it < end:
        return 20
    else:
        return 10

def getValue(name,ls):
    a=filter(lambda (x,y):y.find(name)>=0,ls)
    sum=0
    for i in range(len(a)):
        (c,d)=a[i]
        sum= sum +c
        if len(d)>=100:
            sum = sum+20
        else:
            sum = sum+10
    return sum
    
    
for i in range(n):
    tps.append(ins[1+i].strip().lower())

ids={}

for i in range(m):
    index=2*i+1 +n
    id,tm=ins[2*i+1 +n].split()
    va= getTime(int(tm))
    if id in ids.keys():
        ids[id].append((va,ins[index+1].strip().lower()))
    else:
        ids[id]=[(va,ins[index+1].strip().lower())]
        
res=[]
keys= ids.keys()

for i in range(n):
    maxV =2
    id = -1

    for j in range(len(ids)):
        rs=ids[keys[j]]
        v=getValue(tps[i],rs)
        if v > maxV:
            maxV=v
            id=keys[j]
        if v == maxV:

            if int(id) > int(keys[j]):
                id =keys[j]
    res.append(id)
for i in range(len(res)):
    print res[i]
        
    
https://www.hackerrank.com/contests/booking-passions-hacked-backend/challenges/reviews
Reviews
Guest reviews are an important part of helping travelers choose destinations that satisfy their passions. Each
guest review consists of a reviewer ID ( ), Unix time timestamp denoting the date of the review ( ), and a
string of body text ( ).
To help determine which reviewers are experts on a specific passion, we want to score each reviewer for
their reviews mentioning that passion. A reviewer's score for a single, specific passion is calculated as
follows:
Review Date:
Reviews having a timestamp, , in the inclusive range between June , , and
July , , (GMT) are awarded points.
Reviews written outside of the aforementioned time range (i.e., before or after) are awarded
points.
Review Length:
A review body, , having or more characters is awarded points.
A review having less than characters is awarded points.
If a reviewer has more than one review mentioning a specific passion, their expertise score for that
passion is the sum of the scores for all their reviews mentioning that specific passion.
Determining the foremost expert reviewer with regard to a specific passion:
1. Score Each Reviewer. Note that a reviewer ID may have multiple reviews associated with it and a
reviewer's expertise score for a passion is the sum of the scores for all their reviews mentioning that
passion.
2. Breaking Ties. If two reviewer IDs have the same expertise score for a passion, choose the reviewer
with the smaller ID.
Given a set of reviews and a list of passions, go through each passion (in order) and print the reviewer ID (
) for the reviewer having the highest expertise score for that passion on a new line. If no reviewers
mentioned a specific passion, print instead.
Input Format
The first line contains two positive space-separated integers denoting the respective values of (the
number of passions) and (the number of reviews).
Each line of the subsequent lines contains a single word describing passion .
The subsequent lines describe each of the reviews over two lines:
1. The first line contains two space-separated integers describing the respective values of (the reviewer
ID) and (the review's Unix time timestamp in seconds).
2. The second line contains a string of text denoting the value of (the review's body).
Constraints
String will contain a maximum of characters.
Output Format
Print lines of output. Each line must contain a single integer denoting the reviewer ID ( ) of the expert
for the passion received as input; if no reviewers mentioned that specific passion, print instead.
Sample Input
3 4
Skating
Food
Climbing
1 1467720000
Skating is good in Austria
22 1464782400
I loved the Spanish food, it had so many varieties and it was super super delicious. The price was a little bit high but it was worth it.
People who don't like spicy food might need to think twice as it could be a little bit problematic for them.
4 1467720000
I didn’t like the Indian food!
50 1467720000
People were really friendly, I enjoyed being there.
Sample Output
1
4
-1
Explanation
There are reviews:
1. Reviewer wrote a review on that was less than
characters.
2. Reviewer wrote a review on that was greater than
characters.
3. Reviewer wrote a review on that was less than
characters.
4. Reviewer wrote a review on that was less than
characters.
We then find the highest scoring reviewer for each of the respective passions and print the foremost expert
reviewer's ID on a new line:
1. Reviewer is the only person to mention skating, so they are automatically the highest scoring
reviewer for this passion. Thus, we print on a new line.
2. Reviewers and both mentioned food in their reviews. We calculate their review scores as follows:
Reviewer gets points for having a review with characters and points for writing a
review between June , and July , .
Reviewer gets points for having a review with characters and points for writing a
review before June , .
Because both reviewers scored a total of points, we break the tie by choosing the reviewer having
the smallest ID number ( ); because , we print on a new line.
3. None of the reviewers mentioned climbing, so we print on a new line.