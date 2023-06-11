# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n , m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    result1 = input()
    d[result1].append(i + 1)
    
for _ in range(m):
    result2 = input()
    if result2 not in d:
        print(-1)
    else:
        print(*d[result2])
