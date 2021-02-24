n=int(input())
s=[]
for _ in range(n):
    s_i=input()
    s.append(s_i)
ans=0
for i in range(n)[::-1]:
    if s[i]=="OR":
        ans+=2**(i+1)
ans+=1
print(ans)