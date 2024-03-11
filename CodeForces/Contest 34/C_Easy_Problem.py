from collections import  defaultdict
import sys, threading

sys.setrecursionlimit(1<<30)
threading.stack_size(1<<27)

def main():
    n = int(input())
    s = input()
    arr = list(map(int, input().split()))
    original = "hard"

    memo = {}
    def dp(i, j):
        state = (i, j)
        
        if state in memo:   
            return memo[state]

        if j >= len(original):
            return float("inf")
        
        if i >= len(s):
            return 0

        if s[i] != original[j]:
            memo[state] = dp(i+1, j)
        else:
            memo[state] = min(dp(i+1, j+1), dp(i+1, j) + arr[i])
        
        return memo[state]

    result = dp(0, 0)
    print(result)

main_threading = threading.Thread(target=main)
main_threading.start()
main_threading.join()