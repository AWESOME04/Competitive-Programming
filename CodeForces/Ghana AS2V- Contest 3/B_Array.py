n = int(input())

numbers = list(map(int, input().split()))
negative = []
positive = []
zero = []

for number in numbers:
    if number < 0 and len(negative) < 1:
        negative.append(number)

    elif number > 0:
        positive.append(number)

    elif number or number == 0:
        zero.append(number)

if len(positive) == 0:
    for element in zero:
        if element != 0 and len(positive) < 2:
            positive.append(element)
    for n in positive:
        zero.remove(n)
        # go to the zero array and take two numbers

print(len(negative), *negative, sep=" ")
print(len(positive), *positive, sep=" ")
print(len(zero), *zero, sep=" ")
