t = int(input())

for _ in range(t):
    sentence = input().split()

    new_sentence = [0] * len(sentence)

    for word in sentence:
        idx = 0
        new_word = []
        for char in word:
            if char.isdigit():
                idx = idx * 10 + int(char)
            else:
                new_word.append(char)


        new_sentence[idx - 1] = "".join(new_word)

    print(*new_sentence)
