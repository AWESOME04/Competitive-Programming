def is_square_num(a1, b1, a2, b2):
    if (a1 == a2 and b1 + b2 == a1) or (a1 == b2 and b1 + a2 == a1) or (b1 == a2 and a1 + b2 == b1) or (b1 == b2 and a1 + a2 == b1):
        return True
    else:
        return False


n = int(input())

for _ in range(n):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    if is_square_num(a1, b1, a2, b2):
        print("Yes")
    else:
        print("No")
