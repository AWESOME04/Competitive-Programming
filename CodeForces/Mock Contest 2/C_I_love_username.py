n = int(input())
points = list(map(int, input().split()))


amazing_performances = 0
best_performance = points[0]
worst_performance = points[0]

for i in range(1, n):
    if points[i] > best_performance:
        best_performance = points[i]
        amazing_performances += 1
    elif points[i] < worst_performance:
        worst_performance = points[i]
        amazing_performances += 1

print(amazing_performances)
