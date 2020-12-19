n=int(input())
a=list(map(int,input().split()))
a.sort()
data=[0]*n
ans=0
for i in range(1,len(a)):
    s=data[i-1]
    s+=(a[i]-a[i-1])*i
    data[i]=s
    ans+=s
print(ans)