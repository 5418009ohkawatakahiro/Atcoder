x=list(map(int,input().split()))
if max(x)<min(x)+3:
    print("Yes")
else:
    print("No")