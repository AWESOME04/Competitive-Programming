t = int(input())
for _ in range(t):
    n = int(input())
    arrn = list(map(int, input().split()))
    m = int(input())
    arrm = list(map(int, input().split()))

    arr = []
    prefix = []
    acc = 0

    for i in range(max(len(arrn), len(arrm))):
        if i < len(arrn):
            arr.append(arrn[i])
        if i < len(arrm):
            arr.append(arrm[i])
            
    for num in arr:
        acc += num
        prefix.append(acc)
    
    if max(prefix) < 0:
        print(0)
    else:
        print(max(prefix))

    