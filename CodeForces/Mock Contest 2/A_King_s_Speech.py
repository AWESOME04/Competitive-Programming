words = []
len_words = int(input())
for _ in range(len_words):
    curr_word = input()
    words.append(curr_word)

for value in words:
        print(f"{value[0]}{value[1]}... {value}?")
