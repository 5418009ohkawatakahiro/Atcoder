n,x=map(int,input().split())
s=0.0
ans=-1
x=float(x*100)
for i in range(n):
    v,p=map(int,input().split())
    if x<s:
        continue
    alcohol=v*p
    s+=alcohol
    if x<s:
        ans=i+1
print(ans)