if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records += [[name, score]]
        scores += [score]
    scores.sort()
    second_lowest = scores[0]
    for score in scores:
        if score > scores[0]:
            second_lowest = score
            break
    names_of_second_lowest = [record[0] for record in records if record[1] == second_lowest]
    names_of_second_lowest.sort()
    for name in names_of_second_lowest:
        print(name)
