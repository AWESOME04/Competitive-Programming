num_of_eng = int(input())

roll_num_eng = set(list(map(int, input().split())))

num_of_fr = int(input())

roll_num_fr = set(list(map(int, input().split())))

print(len(roll_num_eng.union(roll_num_fr)))
