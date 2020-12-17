import math
l=int(input())
l-=1
ans=math.factorial(l)//(math.factorial(l-11)*math.factorial(11))
print(ans)