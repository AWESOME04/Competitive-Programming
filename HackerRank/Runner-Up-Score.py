if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr2 = sorted(arr, reverse=True)
    for i,x in enumerate(arr2):
        if max(arr2)==arr2[i]:
            pass
        else:
            print(x)
            break
