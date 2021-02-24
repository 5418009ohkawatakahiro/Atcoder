n,k=map(int,input().split())
ans=n
n=str(n)
for i in range(k):
    a=sorted(n)
    b=sorted(n)[::-1]
    a=int("".join(a))
    b=int("".join(b))
    ans=b-a
    n=str(ans)
print(ans)