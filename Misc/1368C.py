
tt = int(input())
ans = []
ans.append([7 + 3 * (tt - 1)])
for i in range(tt + 2):
    if i == 0:
        ans.append([i, tt + 1 - i])
        ans.append([i, tt + 1 - i - 1])
    elif i == tt + 1:
        ans.append([i, tt + 1 - i + 1])
        ans.append([i, tt + 1 - i])
    else:
        ans.append([i, tt + 1 - i + 1])
        ans.append([i, tt + 1 - i])
        ans.append([i, tt + 1 - i - 1])

for i in ans:
    for a in i:
        print(a, end=" ")
    print()