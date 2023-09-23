n = int(input())
t = list(map(int, input().split()))

l, r = 0, n-1
s_alice, s_bob = 0, 0
a, b = 0, 0

while l <= r:
    if s_alice == s_bob:
        s_alice += t[l]
        l += 1
        a += 1
    elif s_alice < s_bob:
        s_alice += t[l]
        l += 1
        a += 1
    else:
        s_bob += t[r]
        r -= 1
        b += 1

print(a, b)
