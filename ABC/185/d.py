import math
n,m=map(int,input().split())
d=[]
ans=0
if m!=0:
    a=list(map(int,input().split()))
    a.sort()
    if a[0]!=1:
        d.append(a[0]-1)
    for i in range(1,m):
        temp=a[i]-a[i-1]-1
        if temp!=0:
            d.append(temp)
    if a[-1]!=n:
        d.append(n-a[-1])
    if len(d)==0:
        ans=0
    else:
        min_size=min(d)
        for i in d:
            ans+=math.ceil(i/min_size)
else:
    ans=1
print(ans)