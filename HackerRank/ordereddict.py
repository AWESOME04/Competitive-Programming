# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n = int(input())
d = defaultdict(int)

info_list = [input().split() for _ in range(n)]

for info in info_list:
    price = int(info.pop())
    item = ' '.join(info)
    d[item] += price

for k, v in d.items():
    print(k, v)
