n=int(input())
data=[]
a_vote=0
for _ in range(n):
    a,b=map(int,input().split())
    a_vote+=a
    c=a*2+b
    data.append(c)
data.sort()
t_vote=0
ans=0
for i in data[::-1]:
    if t_vote<a_vote:
        ans+=1
        t_vote+=i
    else:
        break
print(ans)