def get_cost(a):
    return int(max(a)) - int(min(a))

for t in range(int(input())):
    a, b = input().split()
    if (len(b) > len(a)):
        print("9" * len(a))
    else:
        ans = a
        for i in range(len(a)):
            for j in range(int(a[i]), int(b[i]) + 1):
                for k in range(10):
                    x = a[:i] + str(j) + str(k) * (len(a) - i - 1)
                    if (a <= x <= b) and (get_cost(x) < get_cost(ans)):
                        ans = x
        print(ans)