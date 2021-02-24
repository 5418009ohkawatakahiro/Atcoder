n=int(input())
a=list(map(int,input().split()))
first=max(a[0:2**n//2])
second=max(a[2**n//2:])
if first<second:
    print(a.index(first)+1)
else:
    print(a.index(second)+1)