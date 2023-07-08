t = int(input())  

for _ in range(t):
    n = int(input()) 
    arr = list(map(int, input().split())) 

    brr = sorted(arr)  

    for i in range(n):
        if arr[i] != brr[n-1]:
            print(arr[i] - brr[n-1], end=" ")
        else:
            print(arr[i] - brr[n-2], end=" ")
    
    print()