n=int(input())
data=[]
for _ in range(n):
    xy=list(map(int,input().split()))
    data.append(xy)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        tilt=(data[i][1]-data[j][1])/(data[i][0]-data[j][0])
        if abs(tilt)<=1:
            ans+=1
print(ans)