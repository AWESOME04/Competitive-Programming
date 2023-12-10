t = int(input())

for _ in range(t):
    ticket = input().strip()
    
    int_ticket = [int(digit) for digit in ticket]

    first_three = sum(int_ticket[:3])
    last_three = sum(int_ticket[3:])

    if first_three == last_three:
        print("YES")
    else:
        print("NO")

