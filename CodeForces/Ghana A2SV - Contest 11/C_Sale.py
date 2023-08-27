n, m = map(int, input().split())  
prices = list(map(int, input().split()))  

prices.sort()

s = 0
for i in range(m):
    if prices[i] >= 0:
        break
    s += prices[i]

print(-s)
