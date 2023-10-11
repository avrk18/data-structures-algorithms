tt = list(map(int, input().split()))
ans = 0
su=[]
mi=[]
for zz in range(0, len(tt)):
    A=list(map(int, input().split()))
    su.append(sum(A))
    mi.append(min(A))
su.sort()
mi.sort()
ans=int(sum(su))-int(2*min(mi[0]+mi[1],su[0]))
print(ans)