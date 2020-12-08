n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
ans[1]=abs(a[1]-a[0])
for i in range(2,n):
    ans[i]=min(ans[i-1]+abs(a[i-1]-a[i]),ans[i-2]+abs(a[i-2]-a[i]))
print(ans[-1])