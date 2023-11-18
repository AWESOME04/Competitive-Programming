t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    if n != 5:
        print("NO")
        continue

    sorted_s = ''.join(sorted(s))

    if sorted_s == "Timru":
        print("YES")
    else:
        print("NO")
