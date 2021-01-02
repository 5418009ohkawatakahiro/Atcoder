n=int(input())
ans=0
for i in range(1,n+1):
    if "7" in list(str(i)) or "7" in list(oct(i)[2:]):
        continue
    ans+=1
print(ans)