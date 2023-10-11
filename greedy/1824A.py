def using_greedy(A,B):
    cc=[]
    m=B.count(-1)
    n=B.count(-2)
    z=0
    for i in range(len(B)):
        if B[i]>0 and B[i] not in cc :
            cc.append(B[i])
    cc.sort()
    if len(cc)==0:
        z=max(m,n)
    elif A[1]-cc[-1]>n and cc[0]>m:
        z=m+n+len(cc)
    else:
        for i in range(len(cc)):
            z=max(z,min(A[1]-cc[i],n+(len(cc)-i-1))+min(cc[i]-1,m+i)+1)
            z=max(z,len(cc)+max(m,n))
    ans.append(min(z,A[1]))


tt = int(input())
ans = []
for zz in range(0, tt):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    using_greedy(A,B)

for i in ans:
    print(i)