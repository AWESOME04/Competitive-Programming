n = int(input())
arts = list(map(int, input().split()))

arts.sort()

least = 1

for art in arts:
    if art > least:
        break
    least += art

print(least)

