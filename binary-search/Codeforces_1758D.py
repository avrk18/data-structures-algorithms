def using_bs(N):
    a = []
    for i in range(N // 2 - 1):
        a.append(N * 4 - 1 - i)
        a.append(N * 4 + 1 + i)
    if N % 2 == 1:
        a.append(N * 4)
    a.append(N * 3)
    a.append(N * 5)
    ans.append(a)

tt = int(input())
ans = []
for zz in range(0, tt):
    N=int(input())
    using_bs(N)

for i in ans:
    for a in i:
        print(a,end=" ")
    print()
