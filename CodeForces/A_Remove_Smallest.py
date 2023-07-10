def is_possible(a):
    if len(a) == 1:
        return True

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if abs(a[i] - a[j]) <= 1:
                a.remove(min(a[i], a[j]))
                return is_possible(a)

    return False


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if is_possible(a) else "NO")
