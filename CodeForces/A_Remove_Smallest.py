for i in range (int(input())):
    input()
    a=list(set([int(i) for i in input().split()]))
    if len(a)==1:
        print("YES")
        continue
    a.sort()
    c=0
    for i in range (len(a)-1):
        if (a[i]+1)!=(a[i+1]):
            print("NO")
            c+=1
            break
    if c==0:
        print("YES")
