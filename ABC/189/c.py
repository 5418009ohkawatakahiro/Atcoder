n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    m=a[i]
    ans=max(ans,m)
    for j in range(i+1,n):
        m=min(m,a[j])
        ans=max(ans,m*(j-i+1))
print(ans)