players = input()
cond = 1

for i in range(1, len(players)):
    if players[i] == players[i-1]:
        cond += 1
        if cond == 7:
            print("YES")
            exit(0)
    else:
        cond = 1
print("NO")