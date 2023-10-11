def using_mis(N):
    a = 0
    b = ""
    if N == 1:
        print("a")
    elif N == 2:
        print("ab")
    else:
        for i in range(1, N + 1):
            if N % i != 0:
                a = i
                break
        for t in range(a):
            b += chr(97 + t)
        e = N // a
        f = N % a
        w = (b * e) + b[:f]
        print(w)

tt = int(input())
ans = []
for zz in range(0, tt):
    N = int(input())
    using_mis(N)
