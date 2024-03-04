from collections import  defaultdict
import sys, threading

sys.setrecursionlimit(1<<30)
threading.stack_size(1<<27)

def main():
    n = int(input())
    graph = defaultdict(list)

    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)

    c = list(map(int, input().split()))

    memo = {}
    def dp(node, parent):
        state = (node, parent)
        if state in memo:
            return memo[(state)]

        for child in graph[node]:
            if child != parent:
                memo[(child, node)] = dp(child, node)
                if c[child - 1] != c[node -1] or not memo[(child, node)]:
                    return False
        return True
    
    flag = False
    for par in range(1, n+1):
        possible = True
        for val in graph[par]:
            possible &= dp(val, par)
        
        if possible:
            flag = True
            print("YES")
            print(par)
            break
    
    if not flag:
        print("NO")

main_threading = threading.Thread(target=main)
main_threading.start()
main_threading.join()





    