
def using_misc(S):
    mx = len(S)
    K = []
    for e in S:
        if e not in K:
            K.append(e)
    for D in K:
        m = 0
        L = S.split(D)
        for a in L:
            if a != "":
                d = len(a)
                if d > m:
                    m = d

        if m < mx:
            mx = m

    if mx == 0:
        ans.append(0)
    else:
        ans.append(int(math.log(mx, 2)) + 1)

import math
tt = int(input())
ans = []
for zz in range(0, tt):
    S = str(input())
    using_misc(S)

for i in ans:
    print(i)