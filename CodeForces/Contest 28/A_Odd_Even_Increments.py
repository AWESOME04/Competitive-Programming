t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    every_even = True
    every_odd = True

    for digit in a:
        if digit % 2 == 0:
            every_odd = False
        else:
            every_even = False

    if every_even or every_odd:
        print("YES")
    else:
        for i in range(1, n, 2):
            a[i] += 1
        
        odd_array = []
        even_array = []

        for val in a:
            if val % 2 == 1:
                odd_array.append(val)
            else:
                even_array.append(val)

        if not odd_array or not even_array:
            print("YES")
        else:
            print("NO")
