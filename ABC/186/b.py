h,w=map(int,input().split())
a=[]
m=100
for i in range(h):
    a_i=list(map(int,input().split()))
    m=min(min(a_i),m)
    a.append(a_i)
ans=0
for H in range(h):
    for W in range(w):
        ans+=(a[H][W]-m)
print(ans)