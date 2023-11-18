k, r = list(map(int, input().split()))

price = 0
val = 0

while True:
    if (price % 10 == 0 and price != 0 ) or price % 10 == r:
        break
    else:
        val += 1
        price += k
print(val)

