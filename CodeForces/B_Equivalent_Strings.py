def equiv_strings(a, b):
    if a == b:
        return True

    sz = len(a)

    if sz % 2 == 1:
        return False

    a1, a2 = a[:sz // 2], a[sz // 2:]
    b1, b2 = b[:sz // 2], b[sz // 2:]

    if (equiv_strings(a1, b2) and equiv_strings(a2, b1)) or (equiv_strings(a1, b1) and equiv_strings(a2, b2)):
        return True
    return False

a = input()
b = input()

if equiv_strings(a, b):
    print("YES")
else:
    print("NO")
