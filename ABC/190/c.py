n,m=map(int,input().split())
ab=[]
ans=0
cnt=0
for _ in range(m):
    ab_i=list(map(int,input().split()))
    ab.append(ab_i)
k=int(input())
dish=[]
for _ in range(k):
    dish_i=list(map(int,input().split()))
    dish.append(dish_i)
data=[0]*(100+1)
for num in range(2**k):
    for i in range(k):
        if ((num>>i)&1==True):
            data[dish[i][0]]=1
        else:
            data[dish[i][1]]=1
    for i in range(m):
        if data[ab[i][0]]==1 and data[ab[i][1]]==1:
            cnt+=1
    ans=max(ans,cnt)
    cnt=0
    data=[0]*(100+1)
print(ans)