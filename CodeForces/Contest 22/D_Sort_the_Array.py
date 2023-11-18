n = int(input())
a = list(map(int, input().split()))

l = 0
r = -1
sorted_a = sorted(a)

if a == sorted(a):
    print("yes")
    print(1, 1)

while a != sorted_a:
    if a[l] < a[r]:
        r -= 1
    if a[l] > a[r]:
        a[l], a[r] = a[r], a[l]
        if a == sorted(a):
            print("yes")
            print(a[l], a[r])
        if a != sorted_a:
            break
        
