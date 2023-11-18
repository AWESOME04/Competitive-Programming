x = input()

res = ""

for num in x:
    comp = min(int(num), 9 - int(num))
    
    res += str(comp)

if res[0] == '0':
    res = '9' + res[1:]

min_num = int(res)

print(min_num)
