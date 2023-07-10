from collections import Counter

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    data = list(map(int, input().split()))

    minimum_cost = 0
    orbit_counts = Counter(data)

    for count in orbit_counts.values():
        minimum_cost += min(count, c)

    print(minimum_cost)
