teams = input()
condition = 1

for i in range(1, len(teams)):
    if teams[i] == teams[i - 1]:
        condition += 1
        if condition == 7:
            print("YES")
            exit()
    else:
        condition = 1

print("NO")
