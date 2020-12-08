n=int(input())
w=list(map(int,input().split()))
s=sum(w)
total=0
ans=s
for i in w[0:-1]:
    total+=i
    ans=min(ans,abs(s-total-total))
print(ans)