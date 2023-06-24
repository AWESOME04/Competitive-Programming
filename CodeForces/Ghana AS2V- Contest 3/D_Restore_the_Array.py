t = int(input())  # Number of test cases
 
for _ in range(t):
    n = int(input())  # Length of array a
    b = list(map(int, input().split()))  # Array b
 
    a = [0] * n  # Initialize array a with zeros
    
    a[0] = b[0]
    a[-1] = b[-1]
    # Set the elements of a based on the differences in b
    for i in range(1,n-1):
        a[i] = min(b[i-1],b[i])
 
    # Print the elements of array a
    print(*a)
