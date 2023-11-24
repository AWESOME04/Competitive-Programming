n, k = map(int, input().split())

h = list(map(int, input().split()))

res= sum(h[:k])
minn = res
ans_ind = 1
l = 0

for r in range(k, len(h)):
    res += h[r] - h[l]
    l += 1
    if res < minn:
        minn = res
        ans_ind = l + 1
print(ans_ind)

