l, r = map(int, input().split())
# res = []
# for i in range(l, r+1):
#     for j in range(l, r+1):
#         res.append(i ^ j)

# print(max(res))

p = l ^ r
x = 1
while x <= p:
    x = x << 1
print(x - 1)