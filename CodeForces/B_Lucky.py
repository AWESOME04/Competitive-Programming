for _ in range(int(input())):
    tickets = input().strip()
    left_sum = 0
    right_sum = 0

    l = 0
    r = -1
    while l < 3 and r  > -4:
        left_sum += int(tickets[l])
        l += 1

        right_sum += int(tickets[r])
        r -= 1
    
    if left_sum == right_sum:
        print("YES")
    else:
        print("NO")
