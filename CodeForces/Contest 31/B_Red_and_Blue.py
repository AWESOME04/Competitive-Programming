t = int(input())
for _ in range(t):
    n = int(input())
    arrn = list(map(int, input().split()))
    m = int(input())
    arrm = list(map(int, input().split()))

    acc_n = 0
    acc_m = 0
    prefix_n = [0]
    prefix_m = [0]
    for num in arrn:
        acc_n += num
        prefix_n.append(acc_n)
    max_n = max(prefix_n)
    
    for num in arrm:
        acc_m += num
        prefix_m.append(acc_m)
    max_m = max(prefix_m)
    
    print(max_m + max_n)