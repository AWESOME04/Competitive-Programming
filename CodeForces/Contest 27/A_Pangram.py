n = int(input())
s = input().lower()

set_s = set(s)

if len(set_s) < 26:
    print("NO")
else:
    print("YES")

