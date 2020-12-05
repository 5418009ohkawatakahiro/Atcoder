import collections
import sys
n=int(input())
t=input()
t=t.split("0")
collection=collections.Counter(t)
ans=0
if n%3==0:
    for key,val in collection.items():
        if key=="11":
            continue
        elif key=="1" and val==2:
            continue
        elif key=="" and val==1:
            continue
        else:
            print(0)
            sys.exit()
elif n%3==1:
    for key,val in collection.items():
        if key=="11":
            continue
        elif key=="1" and val==1:
            continue
        elif key=="" and val==1:
            continue
        else:
            print(0)
            sys.exit()
else:
    for key,val in collections.itmes():
        if key=="11":
            continue
        elif key=="1" and val==1:
            continue
        elif key=="" and val==1:
            continue
        else:
            print(0)
            sys.exit()
l=len(t)
ans=(10**10)-(l-1)
print(ans)