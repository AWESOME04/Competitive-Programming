max = 10**12

cubes = set()
for i in range(1, int(max ** (1/3)) + 1):
    cubes.add(i ** 3)

t = int(input())
for _ in range(t):
    x = int(input())
    yes = False
    for a in range(1, int(x ** (1/3)) + 1):
        if (x - a ** 3) in cubes:
            yes = True
            break
    print("YES" if yes else "NO")


