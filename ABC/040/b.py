import math
n=int(input())
ans=n
for h in range(1,int(math.sqrt(n)+1)):
    for w in range(1,(n//h)+1):
        ans=min(ans,w-h+(n-w*h))
print(ans)