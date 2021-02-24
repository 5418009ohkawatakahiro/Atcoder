import math
n=int(input())
ans=0
while n%2==0:
    n=n//2
for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0:
        ans+=2
if int(math.sqrt(n))*int(math.sqrt(n))==n:
    ans-=1
ans*=2
print(ans)