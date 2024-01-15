t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    s = ''.join(sorted(s))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    index = alphabet.index(s[-1])

    print(index + 1)
