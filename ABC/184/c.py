r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
case1=abs(r1-r2)+abs(c1-c2)
case2=100
if case1%3==0:
    case1=case1//3
else:
    case1=case1//3+1
subr=abs(r1-r2)
subc=abs(c1-c2)
if subr==subc:
    case2=1
else:
    temp=abs(subr-subc)
    if temp%2==0:
        case2=2
    elif temp<=3:
        case2=2
    else:
        case2=3
ans=min(case1,case2)
print(ans)