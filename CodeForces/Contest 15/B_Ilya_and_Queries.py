s = input().strip()
m = int(input().strip())

n = len(s)
cnt = 0
arr = [0] * n

for i in range(1, n):
    if s[i] == s[i - 1]:
        cnt += 1
    arr[i] = cnt

query_results = []
for _ in range(m):
    l, r = map(int, input().strip().split())
    result = arr[r - 1] - arr[l - 1]
    query_results.append(result)

for result in query_results:
    print(result)
