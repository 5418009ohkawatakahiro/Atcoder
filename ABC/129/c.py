n,m=map(int,input().split())
ans=[0]*(n+1)
data=[0]*(n+1)
ans[0]=1
for _ in range(m):
    a=int(input())
    data[a]=1
if data[1]==0:
    ans[1]=1
for i in range(2,(n+1)):
    ans[i]=ans[i-1]+ans[i-2]
    if data[i]==1:
        ans[i]=0
    else:
        ans[i]=ans[i]%(10**9+7)
print(ans[-1])