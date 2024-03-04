from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = False
    nums = []
    
    for num in arr:
        nums.append(num % 10)
    count = Counter(nums) 
    for i in range(10):
        for j in range(10):
            for k in range(10):
                cnt  = count.copy()
                cnt[i] -= 1
                cnt[j] -= 1
                cnt[k] -= 1

                if cnt[i]>=0 and cnt[j]>=0 and cnt[k]>=0 and (i+j+k)%10==3:
                    flag = True
                
                # if i in cnt and cnt[i]>0:
                #     cnt[i] -= 1
                #     if j in cnt and cnt[j]>0:
                #         cnt[j] -= 1
                #         if k in cnt and cnt[k]>0:
                #             cnt[k] -= 1
                #             if (i + j + k) % 10 == 3:
                #                 flag = True


    if flag:
        print("YES")
    else:
        print("NO")
