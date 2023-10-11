def using_misc(n,a):
    x = max(a)
    if x > 0:
        k = a.index(x)
        print(n * 2 + 4)
        for i in range(5):
            print(k + 1, k + 1)
        for i in range(n):
            print(i + 1,k + 1)
        for i in range(1,n):
            print(i + 1,i)
    else:
        print(n - 1)
        for i in range(1,n):
            print(n - i, n - i + 1)

t = int(input())
for v in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    using_misc(n, a)

