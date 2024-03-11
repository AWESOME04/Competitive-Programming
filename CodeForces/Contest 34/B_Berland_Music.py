def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        s = input()
        count = 1
        res = []

        for i, val in enumerate(arr):
            arr[i] = [i, val]
        arr.sort(key=lambda x : x[1])

        for tup in arr:
            if s[tup[0]] == "0":
                tup[1] = count
                count += 1

        for tup in arr:
            if s[tup[0]] == "1":
                tup[1] = count
                count += 1

        arr.sort(key=lambda x: x[0])

        for i, val in arr:
            res.append(val)

        print(*res)

if __name__ == "__main__":
    main()

# Alternative Solution
        # hash = {}
        # res = arr[:]

        # ones = []
        # zeros = []

        # for i in range(n):
        #     hash[arr[i]] = i
        #     if s[i] == '0':
        #         zeros.append(arr[i])
        #     else:
        #         ones.append(arr[i])

        # ones.sort(reverse=True)
        # zeros.sort(reverse=True)
        # arr.sort(reverse=True)

        # l = 0
        # for r in ones:
        #     res[hash[r]] = arr[l]
        #     l += 1

        # for r in zeros:
        #     res[hash[r]] = arr[l]
        #     l += 1

        # print(*res)