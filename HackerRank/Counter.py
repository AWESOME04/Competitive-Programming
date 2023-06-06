# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
n = int(input())
shoe_sizes = Counter(map(int, input().split()))
x = int(input())
earned = 0
for i in range(x):
    size,price= map(int,input().split())
    if shoe_sizes[size] > 0:
        shoe_sizes[size]-=1
        earned += price

print(earned)
 
