import sys, threading

sys.setrecursionlimit(1<<30)
threading.stack_size(1<<27)

def main():
    def dp(i, vitamins):
        if len(set(vitamins)) == 3:
            return 0
        if i == len(arr) :
            return float('inf')
        
        state = (i, vitamins)
        if state not in memo:
            if arr[i][1] not in vitamins:
                memo[state] = min(arr[i][0] + dp(i+1, vitamins+arr[i][1]), dp(i+1, vitamins))
            else:
                memo[state] = dp(i+1, vitamins)
        return memo[state]
        
    n = int(input())
    arr = []
    memo = {}
    for _ in range(n):
        c, s = list(map(str, input().split()))
        arr.append((int(c), s))

    res = dp(0, '')
    if res == float('inf'):
        print(-1)
    else:
        print(res)

if __name__=="__main__":
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    