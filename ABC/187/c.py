import collections
n=int(input())
data=[]
for _ in range(n):
    s=input()
    data.append(s)
counter=collections.Counter(data)
ans="satisfiable"
for key,val in counter.items():
    if key[0]=="!":
        if 1<=counter[key[1:]]:
            ans=key[1:]
print(ans)