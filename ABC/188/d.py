N,C=map(int,input().split())
data=[]
for _ in range(N):
    a,b,c=map(int,input().split())
    data.append([a,c])
    data.append([b+1,-c])
data.sort()
val=data[0][1]
ans=0
for i in range(1,len(data)):
    ans+=min(C,val)*(data[i][0]-data[i-1][0])
    val+=data[i][1]
print(ans)