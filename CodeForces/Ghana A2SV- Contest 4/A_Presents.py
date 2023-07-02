def gift_giving(n, pi):
    gift_givers = [0] * n

    for i in range(n):
        gift_givers[pi[i]-1] = i + 1

    return gift_givers

n = int(input())

pi = list(map(int, input().split()))

result = gift_giving(n, pi)
print(' '.join(map(str, result)))
