n = input()

refined = set(n)

count = 0
for word in refined:
    count += 1

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
